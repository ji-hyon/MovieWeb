<template>
  <div>
      {{ comment.content }}
      {{ comment.created_at }}
      <button @click="deleteComment(comment.id)">삭제</button>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'MovieComment',
  props: {
    comment : {
      type: Object,
      required: true,
    }
  },
  data() {
    return {
      commentId : this.comment.id
    }
  },
  methods: {
    deleteComment() {
      axios({
        method: 'delete',
        url:`${API_URL}/api/v1/comments/${this.commentId}/`,
      })
      .then((res)=> {
        console.log(res);
        this.$emit('comment-deleted', this.comment.id);
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style>

</style>