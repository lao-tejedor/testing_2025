## Testing_2025

*Repositorio para Espacio Curricular de Testing - Escuela PROA - Corral de Bustos*

**2025**

### Requerimientos: 

1. **Organización**: 
	- Debes contar con una carpeta personal donde se escribirán todas tus notas de clase para cada uno de los ejes temáticos.
	- Además, debes crear una carpeta virtual local y una carpeta remota para guardar código, apuntes, y otros materiales relevantes.

2. **Asistencia**: asistir al menos al 70% de las clases para cumplir con los requisitos de asistencia.

3. **Participación Activa**: Se espera que trabajes activamente durante las clases y te involucres en las actividades.

4. **Aprobación de Evaluaciones**:
   - Debes aprobar el proyecto del curso.
   - También debes aprobar las dos evaluaciones con una calificación mínima de 7.


``` JavaScript
// suma.js
function sumar(a, b) {
    return a + b;
}

module.exports = sumar;


// suma.test.js
const sumar = require('./suma');

test('suma 1 + 2 para obtener 3', () => {
    expect(sumar(1, 2)).toBe(3);
});
```

_*lole*_
