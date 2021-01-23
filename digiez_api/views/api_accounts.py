from flask import abort, request, Blueprint
from digiez_api.Models import *


api_accounts = Blueprint('api_accounts', __name__, url_prefix='/api/accounts')


@api_accounts.route('', methods=['GET'])
def get_accounts():
    """
    Get all accounts
    ---
    tags:
            - accounts
    responses:
            200:
                    description: List of accounts
    """
    accounts = Account.query.all()
    accounts = accounts_schema.dump(accounts)
    return {'status': 'success', 'data': accounts}, 200

@api_accounts.route('/<account_id>', methods=['GET'])
def get_account(account_id):
    """
    Get a specific account
    ---
    tags:
            - accounts
    parameters:
            -   in: path
                required: true
                name: account_id
                type: integer
    responses:
            200:
                    description: Account found for given id
            404:
                    description: No Account found for given id
    """
    account = Account.query.get(account_id)
    if not account:
        abort(404)
    account = account_schema.dump(account)
    return {'status': 'success', 'data': account}, 200


@api_accounts.route('', methods=['POST'])
def create_account():
    """
    Create a account
    ---
    tags:
            - accounts
    responses:
            201:
                    description: account created
    """
    json_data = request.get_json(force=True)
    if not json_data:
        return {'message': 'No input data provided'}, 400
    # # Validate and deserialize input
    data = account_schema.load(json_data)
    account = Account.query.filter_by(name=data['name']).first()
    if account:
        return {'message': 'Account already exists'}, 400
    account = Account(
        name=json_data['name']
    )
    account.save()
    # db.session.add(account)
    # db.session.commit()
    #
    result = account_schema.dump(account)
    return {"status": 'success', 'data': result}, 201

@api_accounts.route('/<account_id>', methods=['PUT'])
def edit_account(account_id):
    """
    Edit an account
    ---
    tags:
            - account
    parameters:
            -   in: path
                required: true
                name: account_id
                type: integer
    responses:
            200:
                    description: account edited
            404:
                    description: No account found for given id
    """
    # json_data = request.get_json(force=True)
    # if not json_data:
    #     return {'message': 'No input data provided'}, 400
    # # Validate and deserialize input
    # data = account_schema.load(json_data)
    # # category = Account.query.filter_by(id=data['id']).first()
    # account = Account.query.get(account_id)
    # if not account:
    #     return {'message': 'Category does not exist'}, 400
    # account.name = data['name']
    # db.session.commit()
    data = request.get_json()
    account = Account.query.get(account_id)
    if not account:
        abort(404)
    account.update(data)
    account.save()
    result = account_schema.dump(account)
    return {"status": 'success', 'data': result}, 200


@api_accounts.route('/<account_id>', methods=['DELETE'])
def delete_account(account_id):
    """
    Delete an account
    ---
    tags:
            - accounts
    parameters:
            -   in: path
                required: true
                name: account_id
                type: integer
    responses:
            204:
                    description: Division deleted
            404:
                    description: No account found for given id
    """
    # json_data = request.get_json(force=True)
    # if not json_data:
    #     return {'message': 'No input data provided'}, 400
    # Validate and deserialize input
    # data = account_schema.load(json_data)
    # data, errors = account_schema.load(json_data)
    # if errors:
    #     return errors, 422
    # account = Account.query.filter_by(id=account_id).delete()
    # db.session.commit()

    deleted_count = Account.delete(account_id)
    if not deleted_count:
        abort(404)
    # result = account_schema.dump(account)
    # return {"status": 'success', 'data': result}, 204
    return '', 204
