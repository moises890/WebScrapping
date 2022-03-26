from numpy import var
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd 
import time 


def exelDoc():
    data_frame = {}
    archivo_exel = pd.DataFrame(data_frame)
    archivo_exel.to_excel('ListaPropiedades.xlsx',index=False)


def scrapping():
    Path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(Path)
    driver.get("https://www.bnventadebienes.com/properties/search")
    propiedades = []
    WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.btn btn-primary-action'.replace(' ', '.'))))\
    .click()
    for i in range(1,9):
        WebDriverWait(driver,10)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/div[3]/div[5]/div/div[2]/div[1]/a["+str(i)+"]/div" )))\
        .click()
        texto_div1 = driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div[2]/div/div/div[1]/div[1]/div[11]/div[1]')
        texto_div1 = texto_div1.text.split('\n')

        texto_div2 = driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div[2]/div/div/div[1]/div[1]/div[11]/div[3]')
        texto_div2 = texto_div2.text.split('\n')

        texto_div3 = driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div[2]/div/div/div[1]/div[1]/div[11]/div[5]')
        texto_div3 = texto_div3.text.split('\n')
   
        texto_div4 = driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div[2]/div/div/div[1]/div[1]/div[11]/div[7]/div[3]')
        texto_div4 = texto_div4.text.split('\n')

        texto_div5 = driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div[2]/div/div/div[1]/div[1]/div[12]/div/div/div/div/div[2]/div[6]')
        texto_div5 = texto_div5.text

        texto_div6 = driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div[2]/div/div/div[1]/div[1]/div[12]/div/div/div/div/div[2]/div[7]')
        texto_div6 = texto_div6.text

        texto_div7 = driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div[2]/div/div/div[1]/div[1]/div[12]/div/div/div/div/div[2]/div[8]')
        texto_div7 = texto_div7.text
   
        texto_div8 = driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div[2]/div/div/div[1]/div[1]/div[11]/div[11]')
        texto_div8 = texto_div8.text
   
        marcoDatos = pd.DataFrame.from_dict({'Ubicacion':texto_div1,'Sobre la propiedad':texto_div2,'Caracteristicas':texto_div3,'Descargables':texto_div4,
        'Contacto vendedor':[texto_div5,texto_div6,texto_div7],'descripcion':[texto_div8]},orient='index')
        marcoDatos = marcoDatos.transpose()
        propiedades.append(marcoDatos)
        driver.back()
 
    paginador = pd.ExcelWriter('ListaPropiedades.xlsx')
    num = 1
    for i in propiedades: 
        i.to_excel(paginador,"propiedad"+str(num),index=False)
        num+=1
    paginador.save()
    paginador.close()


exelDoc()
time.sleep(2)
scrapping()
