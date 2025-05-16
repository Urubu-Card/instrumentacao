import blibotecadb as db


def main():

    

    r = "Sim"
    while r=="Sim":
        resp = db.primeiro()
        if resp == 1:
            db.peguntas()
        elif resp == 2:
            db.listar()    


        elif resp == 3:
            db.deletar()

        else:
            db.erro
            
    db.closecon()
main()

