<template>
  <v-card>
    <v-card-title v-if="!updating">Add Organisation</v-card-title>
    <v-card-title v-else>Update Organisation</v-card-title>
    <v-card-text>
      <v-text-field v-model="organisation.name" label="Name" />
      <v-text-field v-model="organisation.address" label="Address" />
      <v-text-field v-model="organisation.city" label="City" />
      <v-text-field v-model="organisation.state" label="State" />
      <v-text-field v-model="organisation.country" label="Country" />
      <v-text-field v-model="organisation.postcode" label="Postcode" />
      <v-text-field v-model="organisation.phone" label="Phone" />
      <v-text-field v-model="organisation.email" label="Email" />
      <v-text-field v-model="organisation.website" label="Website" />
    </v-card-text>
    <v-card-actions>
      <v-btn v-if="!updating" :disabled="lock" color="primary" @click="addOrganisation()">Save</v-btn>
      <v-btn v-else :disabled="lock" color="primary" @click="updateOrganisation()">Update</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: ['organisation_id'],
  data() {
    return {
      organisation: {},
      lock: false,
      updating: false,
    }
  },
  watch: {
    organisation_id() {
      if (this.organisation_id) {
        this.updating = true
        this.getOrganisation(this.organisation_id)
      } else {
        this.updating = false
        this.organisation = {}
      }
    },
  },
  created() {
    if (this.organisation_id) {
      this.updating = true
      this.getOrganisation(this.organisation_id)
    } else {
      this.updating = false
      this.organisation = {}
    }
  },
  methods: {
    async getOrganisation(id) {
      const response = await this.$axios.$get(`/organisation/organisation?id=${id}`)
      this.organisation = response
    },
    async addOrganisation() {
      this.lock = true
      await this.$axios.$post('/organisation/organisation', this.organisation)
      this.lock = false
      this.organisation = {}
      this.$emit('save')
    },
    async updateOrganisation() {
      this.lock = true
      await this.$axios.$put(`/organisation/organisation?id=${this.organisation_id}`, this.organisation)
      this.lock = false
      this.organisation = {}
      this.$emit('save')
    },
  },
}
</script>
