create_passwords_table = """ CREATE TABLE IF NOT EXISTS passwords (
                                        id integer PRIMARY KEY,
                                        user_id integer NOT NULL,
                                        website text NOT NULL,
                                        username text NOT NULL,
                                        password text NOT NULL
                                    ); """

create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        user_id integer PRIMARY KEY,
                                        email text NOT NULL,
                                        password text NOT NULL
                                    ); """
