from dataclasses import dataclass

@dataclass
class DataIngestioArtifact:
    trained_file_path:str
    test_file_path:str
