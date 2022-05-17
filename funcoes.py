from pyodbc import connect


def conectar():
    conexao = None
    try:
        conexao = connect('DSN=folha_pm_balneario_rincao', ConnectionIdleTimeout=0)
    except Exception as error:
        print(f'Erro na conexao com o banco de dado, função "conectar" {error}')
    finally:
        return {'cursor': conexao.cursor(), 'conexao': conexao}


def executar(comando):
    conexao = conectar()
    try:
        conexao['cursor'].execute(comando)
        conexao['conexao'].commit()
    except Exception as error:
        print(f'Erro ao executar SQL, função "executar" {error}')
    finally:
        conexao['cursor'].close()


def consultar(comando):
    conexao = conectar()
    lisaDado = []
    try:
        conexao['cursor'].execute(comando)
        resultado = conexao['cursor'].fetchall()
        for i, descricao in enumerate(resultado):
            lisaDado.append({})
            for j, valor in enumerate([d[0] for d in conexao['cursor'].description]):
                lisaDado[i][valor] = descricao[j]
    except Exception as error:
        print(f'Erro ao consultar o SQL, função "consultar" {error}')
    finally:
        conexao['cursor'].close()
        return lisaDado


def permissao(comando):
    return f"""set option fire_triggers = 'off';
                {comando}
                COMMIT; 
                set option fire_triggers = 'on';"""
