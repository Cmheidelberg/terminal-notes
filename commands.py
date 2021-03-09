import click


@cli.command(short_help="Create a Linux environment to run your model. The working directory selected must"
                                " contain all the files required for the execution of your model")
@click.argument(
                "user_execution_directory",
                type=click.Path(exists=True, dir_okay=True, file_okay=False, resolve_path=True),
                default=Path('.'),
                required=True
                )
@click.option('--name', prompt="Model component name", help="Name of the model component you want for your model")
@click.option('--image',help="(Optional) If you have a DockerImage, you can use it",default=None)
def start(user_execution_directory, name, image):
        """
            This step generates a mic.yaml file and the directories (data/, src/, docker/). It also initializes a local
                GitHub repository

            The argument: `model_configuration_name` is the name of the model component you are defining in MIC
        """
        print("hello world")
