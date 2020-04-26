<template>
    <div>
        <v-container>
            <form @submit.prevent="onSubmit">
                <v-text-field
                    v-model="company_name"
                    label="会社名"
                    required
                ></v-text-field>

                <v-text-field
                    v-model="company_email"
                    label="E-mail"
                    required
                ></v-text-field>

                <v-text-field
                    v-model="job_title"
                    label="職種"
                    required
                ></v-text-field>

                <v-textarea
                    v-model="job_description"
                    label="仕事内容"
                    required
                ></v-textarea>

                <v-text-field
                    v-model="salary"
                    label="給料"
                    required
                ></v-text-field>

                <v-text-field
                    v-model="prefectures"
                    label="都道府県"
                    required
                ></v-text-field>

                <v-text-field
                    v-model="city"
                    label="市町村"
                    required
                ></v-text-field>

                <div class="text-center">
                    <v-btn
                        color="success"
                        type="submit"
                    >送信
                    </v-btn>
                </div>
            </form>
        </v-container>
    </div>
</template>

<script>
import { apiService } from "../common/api.service.js"

export default {
    name: "JobEditor",
      props: {
        id: {
            type: Number,
            required: false
        }
    },
    data() {
        return {
            company_name: null,
            company_email: null,
            job_title: null,
            job_description: null,
            salary: null,
            prefectures: null,
            city: null,
            error: null
        }
    },
    methods: {
        onSubmit() {
            let endpoint = "/api/jobs/";
            let method = "POST";
            if (this.id !== undefined) {
                endpoint += `${this.id}/`;
                method = "PUT";
            }
            apiService(endpoint, method, {
                company_name: this.company_name,
                company_email: this.company_email,
                job_title: this.job_title,
                job_description: this.job_description,
                salary: this.salary,
                prefectures: this.prefectures,
                city: this.city,
            }).then(job_data => {
                this.$router.push({
                    name: 'job',
                    params: { id: job_data.id }
                })
            })
        }
    },
    async beforeRouteEnter (to, from, next) {
        if (to.params.id !== undefined) {
            let endpoint = `/api/jobs/${ to.params.id }/`;
            let data = await apiService(endpoint);
            return next(vm => {
                (vm.company_name = data.company_name),
                (vm.company_email = data.company_email),
                (vm.job_title = data.job_title),
                (vm.job_description = data.job_description),
                (vm.salary = data.salary),
                (vm.prefectures = data.prefectures),
                (vm.city = data.city)
            });
        } else {
            return next();
        }
    },
    created() {
        document.title = "Editor - Job";
    }
}
</script>

<style scoped>

</style>
