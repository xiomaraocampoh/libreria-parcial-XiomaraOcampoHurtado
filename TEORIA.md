## SECCIÓN TEÓRICA — 2.0 puntos
### Archivo: `TEORIA.md` en el repositorio

---

**PREGUNTAS DE SELECCIÓN MÚLTIPLE**
*Escribe el ID de la respuesta correcta y explica en una línea por qué las otras son incorrectas.*

**SM-1 (0.3 puntos)**

Un equipo de desarrollo termina de escribir toda la funcionalidad de un módulo y luego le pide al QA que diseñe las pruebas. Según lo visto en clase, ¿cómo se llama este enfoque y cuál es su principal problema?

A. Shift-left testing. El problema es que las pruebas se vuelven demasiado técnicas para que el cliente las entienda.

B. Shift-right testing. El problema es que las pruebas solo se pueden ejecutar en producción.

**C.** Desarrollo tradicional con pruebas al final. El problema es que los defectos se detectan tarde, cuando corregirlos cuesta hasta 100 veces más que si se hubieran encontrado en etapas tempranas.

D. Integración continua. El problema es que requiere un pipeline de CI/CD que el equipo no tiene configurado.


## Respuesta: C
Concidero que la respuesta correcta es la c ya que segun lo visto en clase el hacer las pruebas al final es desarrollo tradicional que puede generar un alto costo al intentar corregir errores tardios.


---

**SM-2 (0.3 puntos)**

Un desarrollador escribe el siguiente ciclo: primero implementa la función `calcular_descuento()` completa con todos los casos que se le ocurren, luego escribe los tests para verificar que funciona. ¿Qué regla de TDD está violando?

A. La regla del refactor, porque debería mejorar el código antes de escribir tests.

B. La primera regla de Uncle Bob: no escribir código de producción sin que exista primero un test que falle. El código fue escrito antes de que ningún test lo requiriera.

C. La regla del Green, porque el código debería ser mínimo y no cubrir todos los casos desde el inicio.

D. No está violando ninguna regla. TDD permite escribir el código primero siempre que los tests se escriban inmediatamente después.


## Respuesta: B 
concidero que es la b ya que el TDD, esta basado en el principio red-green-refactor que indica que primero debe hacerse las pruebas, las cuales no pasan porque aun no hay codigo.

---

**PREGUNTAS ABIERTAS**
*Responde con tus propias palabras. La extensión ideal es entre 5 y 8 líneas por pregunta. No se piden definiciones de diccionario: se pide que demuestres que entendiste el concepto.*

**PA-1 (0.3 puntos)**

Durante la semana 4 implementamos el carrito de compras con TDD y en el primer ciclo, el paso GREEN consistió en escribir el código más simple posible aunque fuera "feo". Explica por qué TDD obliga a hacer esto en el GREEN y qué pasaría con el proceso si el desarrollador aprovecha ese paso para escribir código "limpio y completo" desde el inicio.

## Respuesta: 
TDD, es decir el test driven development sigue el principio de red-green-refactor lo que obliga a primero hacer las pruebas sin nada de codigo y luego en la etapa de green solo las funcionalidades básicas para que pasen las pruebas, y no hacer todo el  codigo limpio de una ya que esto puede introducir nuevas funcionalidades a las que  aun no se le han hecho pruebas o puede ser  mas complejo descubrir el porque no pasan las pruebas y que esta fallando exactamente, por lo que lo ideal es primero escribir el  codigo básico y luego refactorizar o mejorar ese codigo ya asegurando que las funcionalidades principales funcionann y logrando ver como funcionan.


---

**PA-2 (0.3 puntos)**

Explica con tus propias palabras la diferencia entre TDD y BDD. No es suficiente decir que uno usa código y el otro usa Gherkin. Explica qué problema resuelve cada uno, a quién está dirigido y por qué se complementan en lugar de reemplazarse.

## Respuesta: 

TDD- El test driven develpoment es una meteodologia de desarollo que explica que se deben hacer las pruebas antes de hacer el código mientras que el behavior driven developmente inidica que se debe desarrollar y probar guiados por el comportamiento y en el como deberia actuar el sistema, el test driven delopment soluciona el encontrar bugs o errores en etapas avanzadas del codigo o incluso en produción reduciendo codigo, y el bbd soluciona el hecho de que solo los desaroolladores sepan como esta funcionando el codigo ya que al ser guiado por comportamiento y utilizar gherkin una persona no tecnica puede entender que hace el codigo y como.

---

**PA-3 (0.3 puntos)**

Un compañero te muestra su suite de pruebas y dice: "Tengo 95% de cobertura de código, así que mi sistema no tiene bugs." Explica por qué esa afirmación es incorrecta. Usa un ejemplo concreto que demuestre que cobertura alta no garantiza ausencia de defectos.


## Respuesta: 

---

**PA-4 (0.2 puntos)**

En el contexto de la Regla 2 del examen (descuento entre 0% y 40%), un compañero dice que basta con probar el descuento del 20% porque "si funciona con ese valor, funciona con todos". Explica por qué esa lógica es incorrecta y qué valores concretos deberías probar tú y por qué.

## Respuesta: 

segun lo visto en clase y segun el elder edge o la regla de limites se debe probar con los siguientes valores: justo antes, límites exacto, valor justo después, por tanto se deberia pobar com el 0% el 40%, valor antes del 0, con 39.99% y con 41% y 1%, ya que segun la regal de limites los limites son donde más se ingresan bugs.

---

**PA-5 (0.3 puntos)**

Mirando el planeador de la asignatura, las semanas 3 y 4 cubren pruebas ágiles, TDD y BDD. Explica cómo estas prácticas se conectan con el concepto de CI/CD que veremos en la semana 6. ¿Qué pasaría con un pipeline de CI/CD si el equipo no tiene una suite de tests automatizados sólida?

## Respuesta: 
Basicamente al no haber una suit de pruebas automatizadas solidas, basicamente el pipeline no tendria que ejecutar y si se suben estos cambios sin verificar que no haya errores podemos ingresar los bugs a nuestro sistema ya en producción.


---