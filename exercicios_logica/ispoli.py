class Solution:
    def ispoli(self,x:int)->bool:
        if x is None:
            return x
        frente = str(x) 
        verso = str(x)[::-1]
        if frente == verso:
            return True 
        else:
            return False
