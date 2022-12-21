<template>
  <v-card>
    <v-card-title
      >Organisation List
      <v-btn
        icon
        @click="
          organisation_id = undefined
          dialog = true
        "
        ><v-icon>mdi-plus</v-icon></v-btn
      ></v-card-title
    >
    <v-data-table :headers="headers" :items="organisations">
      <template v-slot:item.active="{ item }">
        <v-btn icon @click="deleteOrganisation(item.id)"><v-icon>mdi-delete</v-icon></v-btn>
        <v-btn
          icon
          @click="
            organisation_id = item.id
            dialog = true
          "
          ><v-icon>mdi-pen</v-icon></v-btn
        >
      </template>
    </v-data-table>
    <v-dialog v-model="dialog">
      <organisation-form
        :organisation_id="organisation_id"
        @save="
          dialog = false
          getOrganisations()
        "
      />
    </v-dialog>
  </v-card>
</template>

<script>
import OrganisationForm from '../components/OrganisationForm.vue'
export default {
  components: { OrganisationForm },

  data() {
    return {
      dialog: false,
      organisation_id: undefined,
      organisations: [],
      headers: [
        { text: 'Name', value: 'name' },
        { text: 'Address', value: 'address' },
        { text: 'City', value: 'city' },
        { text: 'State', value: 'state' },
        { text: 'Country', value: 'country' },
        { text: 'Postcode', value: 'postcode' },
        { text: 'Phone', value: 'phone' },
        { text: 'Email', value: 'email' },
        { text: 'Website', value: 'website' },
        { text: 'Active', value: 'active' },
      ],
    }
  },
  created() {
    this.getOrganisations()
  },
  methods: {
    async getOrganisations() {
      this.organisations = await this.$axios.$get('/organisation/organisations')
    },
    async deleteOrganisation(id) {
      await this.$axios.$delete('/organisation/organisation', { params: { id } })
      this.getOrganisations()
    },
  },
}
</script>
