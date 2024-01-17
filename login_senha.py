#Importando a função sync_playwright da biblioteca playwrigth
from playwright.sync_api import sync_playwright

#Importando a biblioteca time para visualizar a página melhor
import time

#Criando o navegador
with sync_playwright() as p:
    navegador = p.chromium.launch()

    #Criando uma nova página
    pagina = navegador.new_page()
    pagina.goto("http://the-internet.herokuapp.com/") #Sinalizando qual página o código deve direcionar

    #Clicando na opção de preencher formulário
    pagina.locator('xpath=//*[@id="content"]/ul/li[21]/a').click()

    #Espera a página carregar para realizar a próxima ação
    pagina.wait_for_load_state("load")

    #Preenche o login e senha
    pagina.fill('xpath=//*[@id="username"]', 'tomsmith') #Preenche o campo login
    pagina.fill('xpath=//*[@id="password"]', 'SuperSecretPassword!') #Preenche o campo senha
    pagina.locator('xpath=//*[@id="login"]/button/i').click() #Clica para realizar o login

    #Espera a página carregar para realizar a próxima ação
    pagina.wait_for_load_state("load")

    #Realiza uma captura de tela da página
    pagina.screenshot(path="screenshot.png", full_page = True)

    navegador = p.chromium.launch()  # Headless somente para testar se a automação está acontecendo

    # Criando uma nova página
    pagina = navegador.new_page()
    pagina.goto("http://the-internet.herokuapp.com/upload")  # Sinalizando qual página o código deve direcionar

    # Escolhe qual arquivo será escolhido
    pagina.locator('id=file-upload').set_input_files('screenshot.png')

    # Fazendo Upload do arquivo
    pagina.locator('xpath=//*[@id="file-submit"]').click()

    # Espera a página carregar para realizar a próxima ação
    pagina.wait_for_load_state("load")

    # Realiza uma captura de tela da página
    pagina.screenshot(path="screenshot2.png", full_page=True)