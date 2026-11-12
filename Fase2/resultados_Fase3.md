Programa: Fase3/main.py | repetições por arquivo: 5 | Python 3.13.15

| Versão | N | Mediana (ms) | Altura final | Memória pico (KB) | Tempos (ms) |
|---|---|---|---|---|---|
| quase_ordem | 1000 | 12.914 | 11 | 314.6 | 12.983, 12.568, 12.541, 12.914, 15.911 |
| quase_ordem | 5000 | 82.777 | 13 | 1562.0 | 81.395, 82.777, 80.548, 104.678, 98.137 |
| quase_ordem | 20000 | 417.381 | 15 | 6229.8 | 416.907, 417.381, 452.629, 445.693, 416.250 |
| embaralhada | 1000 | 12.821 | 12 | 314.3 | 14.000, 12.821, 12.521, 12.121, 13.717 |
| embaralhada | 5000 | 81.375 | 15 | 1561.4 | 80.808, 82.433, 87.343, 79.573, 81.375 |
| embaralhada | 20000 | 439.800 | 17 | 6202.0 | 439.800, 440.382, 437.920, 434.873, 444.877 |

Razão T(N=20000) / T(N=1000):
- quase_ordem: 32.3
- embaralhada: 34.3

Razão M(N=20000) / M(N=1000):
- quase_ordem: 19.8
- embaralhada: 19.7

Memória pico: maior volume alocado pelo Python durante as operações (tracemalloc), medido em uma execução separada da cronometrada.
