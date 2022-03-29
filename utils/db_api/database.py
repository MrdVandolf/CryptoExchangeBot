from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

import logging
from data import config


class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        try:
            logging.info("Trying to connect to database")
            self.pool = await asyncpg.create_pool(
                user=config.DB_USER,
                password=config.DB_PASS,
                host=config.DB_HOST,
                database=config.DB_NAME
            )
        except asyncpg.InvalidCatalogNameError:
            logging.info("Error: database doesn't exist")
            logging.info("Create new database")
            sys_connection = await asyncpg.connect(
                database="template1",
                user="postgres",
                password=config.DB_PASS
            )

            await sys_connection.execute(
                f"CREATE DATABASE {config.DB_NAME} OWNER {config.DB_USER}"
            )
            await sys_connection.close()
            logging.info("New database created")
            logging.info("Creating connection pool")
            self.pool = await asyncpg.create_pool(
                user=config.DB_USER,
                password=config.DB_PASS,
                host=config.DB_HOST,
                database=config.DB_NAME
            )
            logging.info("Connection pool established. Connection is ok")

    async def execute(self,
                      command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_tables(self):
        managers = """
        CREATE TABLE IF NOT EXISTS Managers(
        id SERIAL PRIMARY KEY,
        telegram_id INTEGER NOT NULL,
        full_name VARCHAR(255) NOT NULL
        );
        """
        requests = """
        CREATE TABLE IF NOT EXISTS Requests(
        id SERIAL PRIMARY KEY,
        type VARCHAR(255) NOT NULL,
        telegram_id INTEGER NOT NULL,
        full_name VARCHAR(255) NOT NULL,
        user_name VARCHAR(255) NOT NULL,
        amount INTEGER NOT NULL,
        status VARCHAR(255) NOT NULL
        );
        """
        courses = """
        CREATE TABLE IF NOT EXISTS Courses(
        id SERIAL PRIMARY KEY,
        course VARCHAR(255) NOT NULL
        )
        """
        for elem in [managers, requests]:
            await self.execute(elem, execute=True)

    async def get_managers_ids(self):
        req = "SELECT telegram_id FROM Managers;"
        res = list(map(lambda x: x[0], await self.execute(req, fetch=True)))
        return res

    async def add_manager(self, tid, full_name):
        req = "INSERT INTO Managers(id, telegram_id, full_name) VALUES ($1, $2, $3);"
        return await self.execute(req, tid, tid, full_name, execute=True)

    async def has_manager(self, tid):
        req = "SELECT * FROM Managers WHERE telegram_id = $1;"
        res = await self.execute(req, tid, fetchval=True)
        return res is not None

    async def add_transaction(self, tid, full_name, user_name, trans_type, crypto_amount):
        req = "INSERT INTO Requests(type, telegram_id, full_name, user_name, amount, status)" \
              " VALUES($1, $2, $3, $4, $5, $6) RETURNING id;"
        res = await self.execute(req, trans_type, tid, full_name, user_name, crypto_amount, "OPEN",
                                 fetchval=True)
        return res

    async def get_transaction(self, id):
        req = "SELECT * FROM Requests WHERE id = $1;"
        res = await self.execute(req, id, fetchrow=True)
        return res

    async def get_transaction_status(self, id):
        req = "SELECT status FROM Requests WHERE id = $1"
        res = await self.execute(req, id, fetchval=True)
        return res

    async def change_transaction_status(self, id, status):
        req = "UPDATE Requests SET status = $1 WHERE id = $2"
        return await self.execute(req, status, id, execute=True)

    async def get_open_transaction_id(self):
        req = "SELECT id FROM Requests WHERE status = $1"
        res = await self.execute(req, "OPEN", fetchval=True)
        return res