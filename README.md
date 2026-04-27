# Radix Sort — Wiki Benchmark

Implementación de **Radix Sort** en Python con benchmark sobre 50,000 números enteros.

---

## ¿Cómo ejecutarlo?

```bash
python radix_sort.py
```

Asegúrate de tener `datos.txt` en la misma carpeta.

---

## Análisis de Complejidad

| Caso | Tiempo | Espacio |
|------|--------|---------|
| Mejor | O(nk) | O(n + k) |
| Promedio | O(nk) | O(n + k) |
| Peor | O(nk) | O(n + k) |

Donde:
- **n** = cantidad de elementos
- **k** = número de dígitos del valor máximo

A diferencia de algoritmos basados en comparaciones (como Merge Sort con O(n log n)),
Radix Sort evita comparar elementos directamente, procesando dígito por dígito.
Esto lo hace **lineal en la práctica** cuando k es pequeño y constante.

---

## Casos de uso ideales

- Listas grandes de **enteros no negativos** con rango acotado
- Ordenamiento de **números de teléfono, IDs, códigos postales**
- Cuando se necesita **estabilidad** (mantiene el orden relativo de elementos iguales)
- Sistemas donde el número de dígitos es pequeño y predecible

## Cuándo NO usarlo

- Datos con negativos (requiere manejo adicional)
- Datos de tipo flotante o cadenas complejas sin adaptación
- Cuando la memoria es muy limitada (usa arreglos auxiliares)

---

## Comparativa: Radix Sort vs Merge Sort

| Criterio | Radix Sort | Merge Sort |
|----------|------------|------------|
| Complejidad tiempo | O(nk) | O(n log n) |
| Complejidad espacio | O(n + k) | O(n) |
| Estable | Sí | Sí |
| Datos requeridos | Solo enteros | Cualquier tipo |
| En la práctica | Muy rápido con k pequeño | Más versátil |

> Para 50,000 enteros de hasta 6 dígitos, Radix Sort tiene ventaja teórica
> sobre Merge Sort porque k=6 hace que O(nk) ≈ O(6n), casi lineal.

---

## Estructura

```
radix-sort-benchmark/
├── README.md
├── radix_sort.py
└── datos.txt
```

---

## Equipo
- Ricardo Emir Pech Tec
- Josué Jared Vazques Dzul
- Gadiel Pech Basulto
