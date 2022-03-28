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
        full_name VARCHAR(255) NOT NULL
        );
        """
        for elem in [managers, requests]:
            await self.execute(elem, execute=True)

