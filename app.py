import pandas as pd

data = {
    "nome": ["Alice", "Bob", "Marquinhos"],
    "idade": [25, 30, 35],
    "estilo": ["Defender", "Defender", "Attacker"]
}

df = pd.DataFrame(data)
display(df)
