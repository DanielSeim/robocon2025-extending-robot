def end_keyword(data, result):
    if result.failed:
        input(f'\nExecution failed: {result.message}\n'
              f'Press enter to continue.')