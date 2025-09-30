from Server.client.src.Python_Agent.agent import generate_linkedin_post

if __name__ == "__main__":
    topic = input("Enter a topic for your LinkedIn post: ")
    post = generate_linkedin_post(topic)
    print("\n--- Generated LinkedIn Post ---\n")
    print(post)
