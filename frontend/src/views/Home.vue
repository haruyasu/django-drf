<template>
	<div class="home">
		<div class="container">
			<h1>Job Boards</h1>
			<div v-for="job in jobs" :key="job.pk">
				<h2>{{ job.company_name }}</h2>
				<p>{{ job.job_title }}</p>
				<hr>
			</div>
		</div>
	</div>
</template>

<script>
import {apiService} from "../common/api.service.js"
export default {
	name: "home",
	data() {
		return {
			jobs: []
		}
	},
	methods: {
		getJobs() {
			let endpoint = "api/jobs/"
			apiService(endpoint).then(data => {
				this.jobs.push(...data.results)
			})	
		}
	},
	created() {
		this.getJobs()
		console.log(this.jobs)
	}
}
</script>
