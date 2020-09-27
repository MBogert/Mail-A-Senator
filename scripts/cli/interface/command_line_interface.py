# command_line_interface.py
import click

@click.command()
@click.argument('name', nargs=1)
@click.argument('template', nargs=-1)
@click.pass_context
def main():
	initialize_session()

def initialize_session():
	
def terminate_session():
	print('term')

if __name__ == "__main__":
	main()