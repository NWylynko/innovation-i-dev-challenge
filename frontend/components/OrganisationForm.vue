<template>
  <v-card>
    <v-card-title>Add Organisation</v-card-title>
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
      <v-btn :disabled="lock" color="primary" @click="addOrganisation()">Save</v-btn>
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
    }
  },
  methods: {
    async addOrganisation() {
      this.lock = true
      await this.$axios.$post('/organisation/organisation', this.organisation)
      this.lock = false
      this.organisation = {}
      this.$emit('save')
    },
  },
}
</script>
