
create_passwords_table = """ CREATE TABLE IF NOT EXISTS passwords (
                                        id integer PRIMARY KEY,
                                        user_id integer NOT NULL,
                                        username text NOT NULL,
                                        password text NOT NULL
                                    ); """
