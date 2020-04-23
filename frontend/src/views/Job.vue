<template>
    <div>
        <div class="container">
            <h1>Job Detail</h1>
            <h2>{{ job.company_name }}</h2>
            <p>{{ job.job_title }}</p>
            <p>{{ job.job_description }}</p>
            <p>{{ job.salary }}</p>
            <p>{{ job.prefectures }}</p>
            <p>{{ job.city }}</p>
        </div>
    </div>
</template>

<script>
import { apiService } from "../common/api.service.js"

export default {
    name: 'Job',
    props: {
        id: {
            type: Number,
            required: true
        }
    },
    data() {
        return {
            job: {}
        }
    },
    methods: {
        setPageTitle(title) {
            document.title = title;
        },
        getJobData() {
            let endpoint = `/api/jobs/${this.id}/`;
            apiService(endpoint).then(data => {
                this.job = data;
                this.setPageTitle(data.company_name);
            })
        }
    },
    created() {
		this.getJobData()
	}
}
</script>

<style>
    
</style>
