<template>
  <div>
    <DetailMovie :movie=movies[movieId-1] />

    <!-- 좋아요 버튼 -->
    <a class="heart-button" @click="[movieLike(), getMovieLike(), getMovieLikeCount()]">
        <i class="heart" :class="liked ? 'bi bi-suit-heart-fill' : 'bi bi-suit-heart'"></i>
    </a> 
    <p>좋아요 : {{ likes_count }}</p>

    <!-- 댓글 입력 창 -->
    <h2 class="comment">댓글</h2>
        <form @submit.prevent="addComment">
            <textarea class="textarea" v-model="newCommentText" placeholder="댓글을 입력하세요" style="width: 50%;"></textarea>
            <button type="submit">댓글 달기</button>
        </form>

    <!-- 댓글 데이터 -->
    <MovieComment v-for = "comment in comments"
      :key="comment.id"
      :comment="comment" 
      @comment-deleted="deleteComment"
    />

    <div v-if="$store.state.token">
        <h2>Comment</h2>
        <form @submit.prevent="addComment">
            <textarea v-model="newCommentText" placeholder="댓글을 입력하세요" style="width: 50%;"></textarea>
            <button type="submit">댓글 달기</button>
        </form>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import DetailMovie from '@/components/DetailMovie.vue'
import MovieComment from '@/components/MovieComment.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'DetailView',
    components: {
        DetailMovie,
        MovieComment,
    },
    created() {
        this.getMovieDetail()
        this.getComments()
        this.getMovieLike()
        this.getMovieLikeCount()
    },
    data() {
        return {
            movieId : this.$route.params.id,
            comments : [],
            newCommentText: '',
  
            // 추가
            likes_count: 0,
            liked: false,
        }
    },
    computed: {
        movies() {
              return this.$store.state.movies
        }
    },
    methods: {
        getMovieDetail() {
            axios({
                method: 'get',
                url: `${API_URL}/api/v1/movies/${this.movieId}/`,
            })
            .then(() => {
                // console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        },

        getComments() {
            axios({
                method: 'get',
                url: `${API_URL}/api/v1/movies/${this.movieId}/comments/`,
            })
            .then((res) => {
                // console.log(res)
                const comments = res.data
                this.comments = comments
            })
            .catch((err) => {
                console.log(err)
            })
        },

        addComment() {
            const movieId = this.movieId
            const content = this.newCommentText  
            const data = {
                movie: movieId,
                content: content
            }
            axios({
                method: 'post',
                url:`${API_URL}/api/v1/movies/${this.movieId}/comments/`,
                data: data,
                headers: {
                    Authorization: `Token ${this.$store.state.token}`
                }
            })
            .then((res) => {
                // console.log(res)
                this.comments.push(res.data)
                this.newCommentText = ''
            })
            .catch((err) => {
                console.log(err)
            })
        },

        deleteComment(deletedCommentId) {
            this.comments = this.comments.filter(comment => comment.id !== deletedCommentId)
        },

        movieLike() {
            axios({
                method: 'post',
                url: `${API_URL}/api/v1/movies/${this.movieId}/like/${this.$store.state.username}/`,
                headers: {
                    Authorization: `Token ${this.$store.state.token}`,
                },
            })
            .then(() => {
                this.getMovieLike()
                this.getMovieLikeCount()
            })     
            .catch((err) => {
                console.log(err)
            })
        },

        getMovieLike() {
            if (this.$store.state.username) {
                axios({
                    method: 'get',
                    url: `${API_URL}/api/v1/movies/${this.movieId}/liked/users/${this.$store.state.username}/`,
                })
                .then((res) => {
                    this.liked = res.data.liked;
                    // console.log(res.data);
                })
                .catch((err) => {
                    console.log(err);
                });
            } else {
                this.liked = false;
            }
        },


        getMovieLikeCount() {
            axios({
            method:'get',
            url:`${API_URL}/api/v1/movies/${this.movieId}/liked/counts/`,
            })
            .then((res) => {
                // console.log(res)
                this.likes_count = res.data.likes_count
                // console.log(res.data)
            })
            .catch((err) => {
                console.log(err)
            })
        },
    }
}
</script>

<style>
.comment {
  color: rgb(153, 78, 153);
  font-family: 'Black Han Sans', sans-serif;
}

.textarea {
    border-radius: 20px;
    border: 2px solid rgb(153, 78, 153);
}

.heart {
    color: red;
}
</style>