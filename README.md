# PYSCRIPT

- O Pyscript permite criar aplicativos Python no navegador usando a interface do `HTML`, `Pyodide`, `WebAssembly` e tecnologias modernas da web. </br>

[pyscript](https://pyscript.net/)

- O pyodide é uma distribuição Python para navegadores e Node.js baseado em WebAssembly. </br>

[pyodide](https://pyodide.org/en/stable/)
[pyodide packages](https://github.com/pyodide/pyodide/tree/main/packages)

- O WebAssembly é um `bytecode (formato de baixo nível mais próximo da linguagem de máquina)` que tem como objetivo desenvolver tecnologias web com melhor performance e disponibilizar recursos nativos na web, isso significa que com o avanço desta tecnologia será possível utilizar programas como Photoshop, autoCAD e até mesmo o ArcGIS Pro diretamente no navegador e não será uma versão web, estaremos executando a versão nativa que atualmente precisamos instalar em nossos computadores, assim não vamos mais precisar instalar estes programas em nossos computadores somente vamos precisar instalar um navegador web, isto é interessante pois uma vez que isso se tornar possível os programas serão compatíveis com todos os sistemas operacionais, pois tudo vai funcionar dentro do navegador. </br>

- O Bytecode é um código intermediário resultado da compilação de uma linguagem que será interpretado por uma máquina virtual para então ser transformado em um código de máquina e em seguida ser interpretado por nossos computadores, assim com o WebAssembly este código intermediário é interpretado pela máquina virtual implementada nos navegadores, permitindo assim que qualquer liguagem que gere este código intermediário possa ser utilizada na Web. </br>

[webassembly](https://webassembly.org/)

Resumindo o Pyscript: </br>
- É um novo framework e está em alpha. </br>
- Permite que você utilize python diretamente no navegador. </br>
- É possível misturar python com javascript. </br>
- Permite acessar qualquer package que esteja disponível no PyPI. </br>
- Permite acessar custom module. </br>
- Permite acessar e controlar o DOM. </br>
- Entre outras coisas. </br>

# INSTALAÇÃO PYSCRIPT

```html
<head>
	<!-- ... -->
  <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
  <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
	<!-- ... -->
</head>
```

# EXEMPLOS PYSCRIPT

**Exemplo 01 - adicionar conteúdos no body ou em elementos**

```html
<body>
	<div
		id="result"
		style="display: grid; place-items: center; color: #eee; background-color: #333;"
	></div>

	<py-script>
		def talk(text): 
			return text 
			
		def scream(function): 
			return lambda text: f"{function(text).upper()} !!!" 
			
		text = "hello world" 
		talk_text = talk(text) 
		print(talk_text) 
		
		currying = scream(talk)
		scream_text = currying(text) 
		print(scream_text) 
		
		pyscript.write("result", f"{talk_text} => {scream_text}")
	</py-script>
</body>
```

**Exemplo 02 - python runtime**

```html
<body>
	<py-script> 
		fruits = ["apple", "banana", "orange"] 
	</py-script>

	<py-repl></py-repl>
</body>
```

**Exemplo 03 importar packages**

```html
<head>
	<!-- ... -->
	<py-env> 
	- emoji 
	</py-env>
</head>
<body>
	<py-script>
		import math 
		import emoji 

		print(math.pi) 
		
		result = emoji.emojize('pyscript é :thumbs_up:') 
		print(result) 

		result = emoji.demojize('pyscript é 👍') 
		print(result)
	</py-script>
</body>
```

**Exemplo 04 arquivos externos**

```html
<head>
	<!-- ... -->
	<py-env> 
	- emoji 
	</py-env>
</head>
<body>
	<main class="container h-screen flex flex-col items-center justify-center">
		<div id="result" class="text-5xl"></div>
	</main>

	<py-script src="./emoji.py"></py-script>
</body>
```

**Exemplo 05 eventos**

```html
<head>
	<!-- ... -->
	<py-env> 
	- emoji 
	</py-env>
</head>
<body>
  <main class="container h-screen flex flex-col items-center justify-center">
    <div id="result" class="text-5xl"></div>
    <button id="btn-result" class="mt-4 p-2 text-white bg-blue-600 rounded" pys-onClick="getEmoji">
      New Emoji
    </button>
  </main>

  <py-script src="./emoji.py"></py-script>
</body>
```

**Exemplo 06 Element**

```html
<head>
	<!-- ... -->
  <link rel="stylesheet" href="./style.css">
  <py-env>
		- paths:
			- ./utils.py
  </py-env>
</head>
<body>
  <main class="container h-screen flex flex-col items-center justify-center">
    <div id="result-py" class="text-5xl font-bold"></div>
    <div id="result-js" class="text-5xl font-bold"></div>
  </main>

  <py-script src="./element.py"></py-script>
</body>
```

**Exemplo 07 Importação de arquivos externos**

```html
<head>
	<!-- ... -->
  <link rel="stylesheet" href="./style.css">
  <py-env>
		- paths:
			- ./utils.py
  </py-env>
</head>
<body>
  <main class="container h-screen flex flex-col items-center justify-center">
    <div id="result-py" class="text-5xl font-bold"></div>
    <div id="result-js" class="text-5xl font-bold"></div>
    <button 
			id="btn-result" 
			class="mt-4 p-2 text-white bg-blue-600 rounded" 
			pys-onClick="toggleColorsHandler"
		>
      Toggle Colors
    </button>
  </main>

  <py-script src="./element.py"></py-script>
</body>
```