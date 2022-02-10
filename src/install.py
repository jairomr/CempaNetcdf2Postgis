from cempa import model
from cempa.db import session


def main():
    # Open the .sql file
    sql_file = open("./metadata/points.sql", "r")
    print(sql_file)
    # Create an empty command string
    sql_command = ""

    # Iterate over all lines in the sql file
    for line in sql_file:
        # Ignore commented lines
        if not line.startswith("--") and line.strip("\n"):
            # Append line to the command string
            sql_command += line.strip("\n")

            # If the command string ends with ';', it is a full statement
            if sql_command.endswith(";"):
                # Try to execute statement and commit it
                try:
                    print("Carregando")
                    session.execute(sql_command)
                    session.commit()

                # Assert in case of error
                except:
                    print("Ops")

                # Finally, clear command string
                finally:
                    sql_command = ""


if __name__ == "__main__":
    main()
