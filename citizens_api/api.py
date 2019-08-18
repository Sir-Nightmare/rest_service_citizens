import logging
import sys

from flasgger import Swagger
from flask import Flask
from flask_restful import Api, Resource

from citizens_api.arg_parser import ArgParser, DEFAULT_HOST

_APP_TITLE = "CitizensAPI"
_APP_VERSION = "0.1.0"

logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format='%(asctime)s - [%(levelname)s] - [%(name)s] - %(message)s')

citizens_app = Flask(__name__)
citizens_app.config["SWAGGER"] = {"title": _APP_TITLE, "version": _APP_VERSION}
api = Api(citizens_app)
swagger = Swagger(citizens_app)


class UploadCitizens(Resource):
    def post(self):
        """
         Import list of citizens to service
         ---
         tags:
           - Base requests
         parameters:
              - name: payload
                in: body
                required: true
         responses:
              201:
                description: List successfully uploaded
              400:
                description: Bad request
              500:
                description: Internal server error
         """
        return {"data": {"import_id": 1}}, 201


class UpdateCitizen(Resource):
    def patch(self, import_id, citizen_id):
        """
        Update info of specified citizen from specified import
        ---
        tags:
           - Base requests
        parameters:
          - in: path
            name: import_id
            type: integer
            required: true
            description: ID of the import
        parameters:
          - in: path
            name: citizen_id
            type: integer
            required: true
            description: ID of the citizen
        responses:
          200:
            description: Citizen info was updated successfully
          400:
            description: Bad request
          404:
            description: Nothing was not found for specified import_id  or citizen_id
          500:
            description: Internal server error
         """
        try:
            import_id = int(import_id)
        except ValueError:
            return {"message": "Invalid import ID"}, 400
        try:
            citizen_id = int(citizen_id)
        except ValueError:
            return {"message": "Invalid import ID"}, 400

        return {'data': {"citizen_id": citizen_id, "import_id": import_id}}, 200


class GetCitizens(Resource):
    def get(self, import_id):
        """
        Get list of citizens from specified import
        ---
        tags:
           - Base requests
        parameters:
          - in: path
            name: import_id
            type: integer
            required: true
            description: ID of the import
        responses:
          200:
            description: OK
          400:
            description: Bad request
          404:
            description: Nothing was not found for specified import_id
          500:
            description: Internal server error
         """
        try:
            import_id = int(import_id)
        except ValueError:
            return {"message": "Invalid import ID"}, 400

        return {'data': [import_id]}, 200


class GetBirthdays(Resource):
    def get(self, import_id):
        """
        Get citizens and number of presents they will buy.
        ---
        tags:
           - Additional requests
        parameters:
          - in: path
            name: import_id
            type: integer
            required: true
            description: ID of the import
        responses:
          200:
            description: OK
          400:
            description: Bad request
          404:
            description: Nothing was not found for specified import_id
          500:
            description: Internal server error
         """
        try:
            import_id = int(import_id)
        except ValueError:
            return {"message": "Invalid import ID"}, 400

        return {'data': [import_id]}, 200


class GetAgeStatistics(Resource):
    def get(self, import_id):
        """
        Get age statistics for each town in import
        ---
        tags:
           - Additional requests
        parameters:
          - in: path
            name: import_id
            type: integer
            required: true
            description: ID of the import
        responses:
          200:
            description: OK
          400:
            description: Bad request
          404:
            description: Nothing was not found for specified import_id
          500:
            description: Internal server error
         """
        try:
            import_id = int(import_id)
        except ValueError:
            return {"message": "Invalid import ID"}, 400

        return {'data': [import_id]}, 200


api.add_resource(UploadCitizens, '/imports')
api.add_resource(UpdateCitizen, '/imports/<import_id>/citizens/<citizen_id>')
api.add_resource(GetCitizens, '/imports/<import_id>/citizens')
api.add_resource(GetBirthdays, '/imports/<import_id>/citizens/birthdays')
api.add_resource(GetAgeStatistics, '/imports/<import_id>/towns/stat/percentile/age')


def run_api():
    logger = logging.getLogger("CitizensAPI")
    logger.info("Starting Citizens API")

    cli_args = ArgParser.parse()
    log_host = "localhost" if cli_args.rest_app_host == DEFAULT_HOST else cli_args.rest_app_host
    logger.info(f"API docs: http://{log_host}:{cli_args.rest_app_port}/apidocs")

    citizens_app.run(host=cli_args.rest_app_host, port=cli_args.rest_app_port, debug=cli_args.is_debug)


if __name__ == "__main__":
    run_api()
