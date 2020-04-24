<template>
    <div>
        <v-container>
            <h2 class="mb-5">{{ job.company_name }}</h2>
            <p>職種：{{ job.job_title }}</p>
            <p>内容：{{ job.job_description }}</p>
            <p>給料：{{ job.salary }}円</p>
            <p>都道府県：{{ job.prefectures }}</p>
            <p>市町村：{{ job.city }}</p>
        </v-container>
    </div>
</template>

<script>
import { apiService } from "../common/api.service.js"

export default {
    name: 'job',
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
