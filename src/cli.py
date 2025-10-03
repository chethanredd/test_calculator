# src/cli.py
import sys
import click
from src.calculator import add, subtract, multiply, divide, power, square_root

@click.command()
@click.argument('operation')
@click.argument('num1', type=float)
@click.argument('num2', type=float, required=False)
def calculate(operation, num1, num2=None):
    try:
        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # Nicely format integers vs floats
        if result == int(result):
            click.echo(int(result))
        else:
            click.echo(f"{result:.2f}")
    except Exception as e:
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    calculate()
