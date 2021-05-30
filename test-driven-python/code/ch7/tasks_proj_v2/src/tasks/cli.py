
if __name__ == '__main__':
    tasks_cli()

@click.group(context_settings={'help_option_names':['-h', '--help']})
@click.version_option(version='0.1.1')
def tasks_cli():
    """Run the tasks application."""
    pass