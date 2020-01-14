#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 08:51:19 2019

@author: matthew

"""


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import sys

"""
O usuario de senha podem ser passados como argumentos atraves do terminal
ex: 
    python sapiens.py ER05002 490760
"""


def main(argv):
    # criando diretorio para salvar o codigo fonte do sapiens
    if not os.path.exists("source-code"):
        os.mkdir("source-code")
     
    try:        
        # verificando se os argumentos foram passados
        aluno = argv[0]
        senha = argv[1]
    except IndexError:
        print("erro! usuário ou senha não informados.")
    
    
    # ocultando navegador
    op = webdriver.FirefoxOptions()
    op.add_argument('-headless')
    
    driver = webdriver.Firefox(options=op)
    
    # indo para pagina do sapiens
    driver.get("https://sapiens.dti.ufv.br/sapiens_crp/CheckLogin.asp")
    # encontrando input de usuario
    elem = driver.find_element_by_id("Usuario")
    elem.clear()
    elem.send_keys(aluno)
    
    
    time.sleep(2)
    
    # input de senha
    elem = driver.find_element_by_id("Senha")
    elem.clear()
    
    elem.send_keys(senha)
    
    time.sleep(2)
    
    elem.send_keys(Keys.RETURN)
    
    driver.get("https://sapiens.dti.ufv.br/sapiens_crp/aluno/avaliacoes.asp")
    
    os.chdir(os.getcwd() + "/source-code")
    
    
    html = driver.page_source
    with open("page_source.html", "w") as f:
        f.write(html)
    
    print("Everything is done!")

if __name__ == "__main__":
    main(sys.argv[1:])

