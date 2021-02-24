import click


class OtherClass:
    '''模拟其他模块的测试类
    '''

    def __init__(self):
        pass


class Context:
    '''命令上下文,如果需要在父命令和子命令之间传递数据这将会非常有用
    '''

    def __init__(self, data):
        self.data = data
        self.oc = OtherClass()


@click.group()
@click.option('-d', '--data', type=str, help='option for test data')
@click.pass_context
def cli(ctx, data):
    '''嵌套命令示例
    '''
    ctx.obj = Context(data)


@cli.command()
@click.pass_context
def subcommand1(ctx):
    '''第一个子命令
    '''
    click.echo('子命令1')
    click.echo(f'测试数据: {ctx.obj.data}')


@cli.command()
@click.pass_context
def subcommand2(ctx):
    '''第二个子命令
    '''
    click.echo('子命令2')
    click.echo(f'测试数据: {ctx.obj.data}')
