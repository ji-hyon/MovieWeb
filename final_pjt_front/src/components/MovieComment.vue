<template>
  <div>
    <div v-if="!isEditing">
      {{ editedComment.content }}
      {{ editedComment.created_at }}
      <button @click="deleteComment(editedComment.id)">삭제</button>
      <button @click="editComment">수정</button>
    </div>
    <div v-else>
      <textarea v-model="editedComment.content" placeholder="댓글을 입력하세요"></textarea>
      <button @click="saveComment">저장</button>
      <button @click="cancelEdit">취소</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieComment',
  props: {
    comment: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      isEditing: false,
      editedComment: {},
    }
  },

  mounted() {
    this.editedComment = Object.assign({}, this.comment);
  },

  methods: {
    deleteComment(commentId) {
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/comments/${commentId}/`,
      })
      .then(() => {
        this.$emit('comment-deleted', commentId);
      })
      .catch(err => console.log(err))
    },

    editComment() {
      this.isEditing = true;
    },

    saveComment() {
      axios({
        method: 'put',
        url: `${API_URL}/api/v1/comments/${this.editedComment.id}/update/`,
        data: {
          content: this.editedComment.content,
        },
      })
        .then((res) => {
          this.$emit('comment-updated', res.data)
          this.isEditing = false;
        })
        .catch(err => console.log(err))
    },

    cancelEdit() {
      this.isEditing = false
    },
  }
}
</script>

<style>
</style>
