<template>
  <div>

    <div v-if="!isEditing"> 
      <span class="name">{{ comment.user.username }}&nbsp;</span>
      <span class="comment"> "{{ editedComment.content }}"</span>
      &nbsp;
      <span class="date"> [{{ editedComment.created_at.slice(0, 19) }}]&nbsp;&nbsp;</span>
      <button class="w-btn-gra1" @click="deleteComment(editedComment.id)" v-show="btn_check">삭제</button>
      <button class="w-btn-gra1" @click="editComment" v-show="btn_check">수정</button>
    </div>
    <div v-else>
      <textarea v-model="editedComment.content" placeholder="댓글을 입력하세요"></textarea>
      <button class="w-btn-gra1" @click="saveComment">저장</button>
      <button class="w-btn-gra1" @click="cancelEdit">취소</button>
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
      btn_check: false,
    }
  },

  created() {
    this.editedComment = Object.assign({}, this.comment);
    this.btn_check = this.$store.state.username === this.editedComment.user.username;
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

<style scoped>
.w-btn-gra1 {
    background: linear-gradient(-45deg, #33ccff 0%, #ff99cc 100%);
    color: white;
    border-radius: 7px;
    border-color: rgb(196, 104, 196);;
    padding: 4px;
    margin: 2px;
    /* margin-top: 10px; */
    display: inline;
}
.name {
  font-weight: bold;
  color: purple;
}

.comment {
  font-weight: 550;
  color: rgb(143, 64, 143)
}

.date {
  color: rgb(143, 64, 143)
}
</style>