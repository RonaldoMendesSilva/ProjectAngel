# coding: utf-8

class Ocorrencia:

  def __init__(self, bombeiro, guarnicao, endereco_ocorr, bairro_ocorr, municipio_ocorr, status, custodia_id_custodia, unid_saude_id_unid_saude, natureza_id_natureza, usuario_id_usuario, usuario_cadvit_pessoa_id, usuario_cadvit_pessoa_envolvidos_ocorr_id_envolvidos):
    self.bombeiro = bombeiro
    self.guarnicao = guarnicao
    self.endereco_ocorr = endereco_ocorr
    self.bairro_ocorr = bairro_ocorr
    self.municipio_ocorr = municipio_ocorr
    self.status = status
    self.custodia_id_custodia = custodia_id_custodia
    self.unid_saude_id_unid_saude = unid_saude_id_unid_saude
    self.natureza_id_natureza = natureza_id_natureza
    self.usuario_id_usuario = usuario_id_usuario
    self.usuario_cadvit_pessoa_id = usuario_cadvit_pessoa_id
    self.usuario_cadvit_pessoa_envolvidos_ocorr_id_envolvidos = usuario_cadvit_pessoa_envolvidos_ocorr_id_envolvidos

  def get_status(self):
    return self.status

  def set_status(self, status):
    self.status = status
