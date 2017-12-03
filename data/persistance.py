import sys
sys.path.append('/nequithon/nequithonpolla/model/')
import sqlite3
class Persistnace:
    def __init__(self):
        con = sqlite3.connect("nequi")
        cur = con.cursor()
        seqid_metas=2

    def crearMeta(self,nombre,valor,fechalimite):
        meta = (self.seqid_metas ,nombre,valor,fechalimite)
        self.cur.execute("insert into metas (id ,nombre ,valor ,fechalimite ) values (?,?,?,?)", meta)
    def asociarUsuariosAMeta(self,id_usuario,id_meta):
        metausuario=(id_usuario,id_meta,0)

    def incrementarProcMeta(self):
        return