<template>
  <section id="hero">
    <video-bg
    :sources="['https://static.videezy.com/system/resources/previews/000/033/930/original/close_up_foot_running1.mp4']" 
    img="https://static.videezy.com/system/resources/previews/000/033/930/original/close_up_foot_running1.mp4"
    class="background-video white--text"
    aspect-ratio="12"
    >
      <v-container class="fill-height px-4 py-12 mt-12 pt-12">
        <v-responsive
          class="d-flex align-center"
          height="100%"
          max-width="700"
          width="100%"
        >
          <base-heading title="실시간 화상PT로 피드백을 받아보세요" />

          <base-body>
            실시간 Online Training, 다같이 운동하면서, 동기부여를 받아보세요
          </base-body>

          <div
            :class="$vuetify.breakpoint.smAndDown ? 'flex-column align-start' : 'align-center'"
            class="d-flex flex-wrap"
          >
            <base-btn @click="gomembership">
              Discover More
            </base-btn>

            <span class="font-weight-bold ml-6 mr-4 my-4">or</span>

            <base-btn
              :ripple="false"
              class="pa-1"
              height="auto"
              color="accent"
              text
              @click="gomembership"
            >
              Get Started Now
            </base-btn>
          </div>
        </v-responsive>
      </v-container>
    </video-bg>
  </section>
</template>

<script>
  export default {
    name: 'HomeHeadline',
    methods: {
      gomembership() {
        this.$router.push('/membership')
      }
    },
    computed: {
      minHeight () {
        const height = this.$vuetify.breakpoint.mdAndUp ? '100vh' : '50vh'
        return `calc(${height} - ${this.$vuetify.application.top}px)`
      },
    }
  }
</script>
<style scoped>
    .background-video {
        opacity: 0.81;
    }
</style>