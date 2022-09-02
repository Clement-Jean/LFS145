const {argv, exit} = require('process')

function main() {
	if (argv.length != 3) {
		console.log('Usage: main.py [fn]')
		exit(1)
	}

	switch (argv[2]) {
		default:
			console.log(`Unknown function: \"${argv[2]}\"`)
			break;
	}
}

main()