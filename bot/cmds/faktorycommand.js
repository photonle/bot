const Command = require("discord.js-commando").Command
const faktory = require("faktory-worker")

module.exports = class FaktoryCommand extends Command {
	async queue(job, data = {}){
		let client = await faktory.connect()
		await client.job(job, data).push()
		await client.close()
	}
}