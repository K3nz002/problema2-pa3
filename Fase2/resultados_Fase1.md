Programa: Fase1/main.py | repetições por arquivo: 5 | Python 3.13.15

| Versão | N | Mediana (ms) | Altura final | Memória pico (KB) | Tempos (ms) |
|---|---|---|---|---|---|
| quase_ordem | 1000 | 57.655 | 889 | 226.0 | 56.661, 63.702, 57.940, 57.655, 56.569 |
| quase_ordem | 5000 | 1725.227 | 4458 | 1058.5 | 1652.095, 1735.393, 1700.903, 1725.227, 1779.642 |
| quase_ordem | 20000 | 30460.668 | 17750 | 4069.3 | 27779.419, 31048.332, 30460.668, 29778.563, 32550.561 |
| embaralhada | 1000 | 8.877 | 22 | 225.7 | 9.823, 8.877, 9.317, 8.823, 8.510 |
| embaralhada | 5000 | 198.547 | 30 | 1058.2 | 185.500, 198.547, 182.065, 206.404, 201.488 |
| embaralhada | 20000 | 3712.773 | 32 | 4041.7 | 5085.300, 5183.345, 3712.773, 3593.994, 3488.849 |

Razão T(N=20000) / T(N=1000):
- quase_ordem: 528.3
- embaralhada: 418.2

Razão M(N=20000) / M(N=1000):
- quase_ordem: 18.0
- embaralhada: 17.9

Memória pico: maior volume alocado pelo Python durante as operações (tracemalloc), medido em uma execução separada da cronometrada.
