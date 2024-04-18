# !/usr/bin/python3
'''**********************************************************************************
                                                                                    *
Project Name: cosmos_delegate_msg.py                                *
                                                                                    *
Programming Language: Python 3.11                                                   *
                                                                                    *
Libraries: json                                                                     *
                                                                                    *
Creater Name: Ziqi Yang                                                             *
                                                                                    *
Published Date: 4/15/2024                                                           *
                                                                                    *
Version: 1.0                                                                        *
                                                                                    *
                                                                                    *
                                                                                    *
                                                                                    *
                                                                                    *
**********************************************************************************'''

#    Scripts start below
from functions import create_connection
import json

def main(tx_id, tx_type, message, ids):

    # import the login info for psql from 'info.json'
    with open('info.json', 'r') as f:
        info = json.load(f)

    db_name = info['psql']['db_name']
    db_user = info['psql']['db_user']
    db_password = info['psql']['db_password']
    db_host = info['psql']['db_host']
    db_port = info['psql']['db_port']

    connection = create_connection(db_name, db_user, db_password, db_host, db_port)
    cursor = connection.cursor()
    try:

        # Define the values
        tx_denom = message['amount']['denom']
        amount = message['amount']['amount']
        message = json.dumps(message)

        #  Edit the query that will be loaded to the database
        query = """
        INSERT INTO cosmos_delegate_msg (tx_id, tx_type, delegator_address_id, validator_address_id, tx_denom, amount, message_info) VALUES (%s, %s, %s, %s, %s, %s,%s);
        """

        values = (tx_id, tx_type, ids['delegator_address_id'], ids['validator_address_id'], tx_denom, amount, message)
        cursor.execute(query, values)

        connection.commit()
        connection.close()
    except KeyError:
        print(f'KeyError happens in type {tx_type}')

if __name__ == '__main__':
    main(tx_id, tx_type, message, ids)