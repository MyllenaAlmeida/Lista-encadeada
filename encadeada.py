class No:
        def __init__(self,item=None,proximo=None):
                self.item=item
                self.proximo=proximo

class Lista:
        def __init__(self):
                '''A lista vazia é criada aqui.'''
                self.primeiro=No()
                self.ultimo=self.primeiro

        def vazia(self):
                '''Se primeiro e último estiverem na mesma
                posição, isso quer dizer que a lista está vazia, pois
                quando um item é adicionado um desses "ponteiros" são movidos.'''
                return self.primeiro==self.ultimo

        def inserir(self,item):
                self.ultimo.proximo=No(item,None)
                self.ultimo=self.ultimo.proximo

        def inserirInicio(self,item):
                self.primeiro.proximo=No(item,self.primeiro.proximo)
                if self.vazia():
                        self.ultimo=self.primeiro.proximo

        def inserirOrdenado(self,item):
                if self.vazia():
                        self.inserir(item)
                anterior=self.primeiro
                atual=self.primeiro.proximo
                while atual is not None and atual.item<item:
                        anterior=atual
                        atual=atual.proximo

                anterior.proximo=No(item,atual)
                if atual is None:
                        self.ultimo=anterior.proximo

        def buscar(self,item):
                if self.vazia():
                        mensagem="Lista vazia."
                        return mensagem
                busca=self.primeiro.proximo
                while busca is not None and busca.item!=item:
                        busca=busca.proximo
                try:
                        if busca.item==item:
                                return True
                except:
                        return False

        def removerInicio(self):
                if self.vazia():
                        mensagem="Lista vazia."
                        return mensagem
                remove=self.primeiro.proximo
                self.primeiro.proximo=remove.proximo
                item=remove.item
                if self.ultimo==remove:
                        self.ultimo=None
                        self.primeiro=None
                remove.proximo=None
                del remove
                return item

        def removerFim(self):
                if self.vazia():
                        mensagem="Lista vazia."
                        return mensagem
                remove2=self.primeiro
                while remove2.proximo != self.ultimo:
                        remove2=remove2.proximo
                item=self.ultimo.item
                ultimo=remove2
                remove2=ultimo.proximo
                ultimo.proximo=None
                del remove2
                return item
                
                        
                
                
                        
        
                
        


