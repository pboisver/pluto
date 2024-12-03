from kgrid import Ko

class HangnailDiagnoser(Ko):
    metadata_file = "metadata4.json"

        
    @staticmethod
    def hangnail(size: float, pain: int):  # Should this be static?
        
        return 50 <= (size * pain)
    

        

