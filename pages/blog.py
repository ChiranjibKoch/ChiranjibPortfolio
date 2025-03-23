import streamlit as st
import pandas as pd
from datetime import datetime
from utils.visitor_counter import display_visitor_counter

# Page configuration
st.set_page_config(
    page_title="Tech Blog - Chiranjib Koch",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar for navigation
with st.sidebar:
    st.title("Navigation")
    st.page_link("app.py", label="Home", icon="🏠")
    st.page_link("pages/skills.py", label="Skills & Expertise", icon="📊")
    st.page_link("pages/projects.py", label="Projects", icon="💻")
    st.page_link("pages/blog.py", label="Tech Blog", icon="📝")
    st.page_link("pages/contact.py", label="Contact", icon="📧")
    
    st.divider()
    st.caption("© 2023 Chiranjib Koch")

# Main content
st.title("Technical Blog")
st.markdown("""
Welcome to my technical blog, where I share insights, tutorials, and thoughts about AI, 
Machine Learning, Python development, MongoDB, and Telegram bot creation.
""")

# Blog post data
blog_posts = [
    {
        "title": "Building Effective Recommendation Systems with TensorFlow",
        "date": "2023-10-15",
        "category": "AI/ML",
        "tags": ["TensorFlow", "Recommendation Systems", "Deep Learning"],
        "content": """
        ## Building Effective Recommendation Systems with TensorFlow
        
        Recommendation systems are a critical component of modern digital platforms, helping users discover content, 
        products, or services that match their interests and preferences. In this article, I'll walk through the 
        process of building an effective recommendation system using TensorFlow.
        
        ### Types of Recommendation Approaches
        
        There are generally three main approaches to building recommendation systems:
        
        1. **Content-based filtering**: Recommends items similar to what a user has liked before
        2. **Collaborative filtering**: Recommends items that similar users have liked
        3. **Hybrid approaches**: Combines content-based and collaborative filtering techniques
        
        ### Collaborative Filtering with TensorFlow
        
        In this tutorial, I'll focus on implementing a collaborative filtering model using TensorFlow's 
        Recommendation System library. This approach learns patterns from user-item interactions to make predictions.
        
        The key steps include:
        
        - Preparing user-item interaction data
        - Embedding users and items in a latent space
        - Training a neural network to predict ratings or interactions
        - Evaluating and fine-tuning the model
        - Serving the model for real-time recommendations
        
        ### Model Architecture
        
        Our model architecture uses embedding layers to represent users and items in a lower-dimensional space:
        
        ```python
        # Create model inputs
        user_id_input = tf.keras.layers.Input(shape=(1,), name='user_id', dtype=tf.int32)
        item_id_input = tf.keras.layers.Input(shape=(1,), name='item_id', dtype=tf.int32)
        
        # Create embeddings
        user_embedding = tf.keras.layers.Embedding(
            num_users, embedding_dim, embeddings_initializer='he_normal',
            embeddings_regularizer=tf.keras.regularizers.l2(1e-6)
        )(user_id_input)
        
        item_embedding = tf.keras.layers.Embedding(
            num_items, embedding_dim, embeddings_initializer='he_normal',
            embeddings_regularizer=tf.keras.regularizers.l2(1e-6)
        )(item_id_input)
        ```
        
        After training, we can use these embeddings to find similar items or make personalized recommendations.
        
        ### Handling Cold Start Problems
        
        One of the challenges in recommendation systems is the "cold start" problem - how to make recommendations 
        for new users or items. I've found that incorporating additional features about users and items can help 
        address this issue.
        
        ### Conclusion
        
        TensorFlow provides powerful tools for building scalable recommendation systems. By leveraging deep learning 
        techniques, we can create personalized experiences that improve user engagement and satisfaction.
        
        In future posts, I'll explore more advanced topics like multi-task learning for recommendations and 
        incorporating contextual information into the recommendation process.
        """
    },
    {
        "title": "Advanced MongoDB Aggregation Pipelines for Data Analysis",
        "date": "2023-09-22",
        "category": "Database",
        "tags": ["MongoDB", "Data Analysis", "Aggregation Framework"],
        "content": """
        ## Advanced MongoDB Aggregation Pipelines for Data Analysis
        
        MongoDB's aggregation framework is a powerful tool for data processing and analysis directly within your database. 
        In this post, I'll share some advanced techniques for building efficient and effective aggregation pipelines.
        
        ### Beyond Basic Aggregations
        
        While simple group and sum operations are useful, the real power of MongoDB's aggregation framework lies in 
        its ability to perform complex transformations and analyses. Let's explore some advanced features:
        
        ### Using $lookup for Joins
        
        The `$lookup` stage allows you to perform left outer joins to other collections:
        
        ```javascript
        db.orders.aggregate([
          {
            $lookup: {
              from: "inventory",
              localField: "item",
              foreignField: "sku",
              as: "inventory_docs"
            }
          }
        ])
        ```
        
        This is especially useful when you need to combine data from multiple collections for analysis.
        
        ### Window Functions with $setWindowFields
        
        MongoDB 5.0 introduced window functions via the `$setWindowFields` stage, enabling advanced analytical capabilities:
        
        ```javascript
        db.sales.aggregate([
          {
            $setWindowFields: {
              partitionBy: "$region",
              sortBy: { date: 1 },
              output: {
                cumulativeQuantity: {
                  $sum: "$quantity",
                  window: {
                    documents: ["unbounded", "current"]
                  }
                }
              }
            }
          }
        ])
        ```
        
        This allows for running totals, moving averages, and other time-series analyses.
        
        ### Optimizing Aggregation Performance
        
        For large datasets, performance matters. Here are some tips:
        
        1. **Use appropriate indexes**: Ensure the fields used in $match, $sort, and $lookup stages are indexed
        2. **Filter early**: Place $match stages as early as possible to reduce the documents processed
        3. **Project only needed fields**: Use $project to limit the fields carried through the pipeline
        4. **Consider memory limitations**: Use $limit and $sample when working with large datasets
        
        ### Real-world Example: Customer Cohort Analysis
        
        One powerful application is customer cohort analysis. Here's a simplified pipeline:
        
        ```javascript
        db.purchases.aggregate([
          // Extract the cohort month from first purchase
          {
            $group: {
              _id: "$customer_id",
              first_purchase: { $min: "$purchase_date" },
              purchases: { $push: { date: "$purchase_date", amount: "$amount" } }
            }
          },
          // Add cohort information
          {
            $addFields: {
              cohort_month: { $dateToString: { format: "%Y-%m", date: "$first_purchase" } }
            }
          },
          // Group by cohort and calculate retention
          {
            $unwind: "$purchases"
          },
          {
            $addFields: {
              purchase_month: { $dateToString: { format: "%Y-%m", date: "$purchases.date" } },
            }
          },
          {
            $group: {
              _id: {
                cohort: "$cohort_month",
                purchase_month: "$purchase_month"
              },
              customer_count: { $sum: 1 },
              revenue: { $sum: "$purchases.amount" }
            }
          },
          { $sort: { "_id.cohort": 1, "_id.purchase_month": 1 } }
        ])
        ```
        
        This pipeline segments customers by their first purchase month and tracks their subsequent purchasing behavior.
        
        ### Conclusion
        
        MongoDB's aggregation framework continues to evolve, offering increasingly sophisticated analytical capabilities. 
        By mastering these advanced techniques, you can perform complex analyses directly in your database, reducing the 
        need for external processing and improving performance.
        """
    },
    {
        "title": "Creating Interactive Telegram Bots with Python",
        "date": "2023-08-10",
        "category": "Telegram",
        "tags": ["Python", "Telegram", "Bot Development"],
        "content": """
        ## Creating Interactive Telegram Bots with Python
        
        Telegram bots provide a powerful way to automate tasks, deliver services, and interact with users. In this guide, 
        I'll walk through the process of building a feature-rich Telegram bot using Python.
        
        ### Getting Started with the Telegram Bot API
        
        First, you'll need to create a bot and get an API token:
        
        1. Contact the BotFather (@BotFather) on Telegram
        2. Send the command /newbot and follow the instructions
        3. Save the API token you receive
        
        ### Setting Up Your Python Environment
        
        I recommend using the python-telegram-bot library, which provides a clean, Pythonic interface to the Telegram Bot API:
        
        ```python
        # Installation
        pip install python-telegram-bot
        
        # Basic bot structure
        from telegram import Update
        from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
        
        # Define a command handler
        async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
            await update.message.reply_text('Hello! I am your bot assistant.')
        
        # Set up the application
        def main() -> None:
            application = Application.builder().token("YOUR_TOKEN").build()
            
            # Add handlers
            application.add_handler(CommandHandler("start", start))
            
            # Run the bot
            application.run_polling()
        
        if __name__ == "__main__":
            main()
        ```
        
        ### Adding Interactive Features
        
        A great bot should be interactive and responsive. Here are some features you can implement:
        
        #### Conversation Handlers
        
        Conversation handlers allow you to create multi-step interactions:
        
        ```python
        from telegram.ext import ConversationHandler, CallbackQueryHandler
        
        # States
        CHOOSING, TYPING = range(2)
        
        async def start_conversation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
            keyboard = [
                [InlineKeyboardButton("Option 1", callback_data='1')],
                [InlineKeyboardButton("Option 2", callback_data='2')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text("Choose an option:", reply_markup=reply_markup)
            return CHOOSING
        ```
        
        #### Inline Keyboards and Callbacks
        
        Inline keyboards provide a clean way for users to interact with your bot:
        
        ```python
        async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
            query = update.callback_query
            await query.answer()
            
            if query.data == '1':
                await query.edit_message_text("You selected Option 1!")
            elif query.data == '2':
                await query.edit_message_text("You selected Option 2!")
        ```
        
        ### Integrating with External Services
        
        Bots become truly powerful when they connect to other services:
        
        #### MongoDB Integration
        
        ```python
        from pymongo import MongoClient
        
        client = MongoClient('mongodb://localhost:27017/')
        db = client['bot_database']
        users_collection = db['users']
        
        async def save_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
            user = update.effective_user
            users_collection.update_one(
                {'user_id': user.id},
                {'$set': {
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_seen': datetime.now()
                }},
                upsert=True
            )
        ```
        
        #### API Integration
        
        ```python
        import aiohttp
        
        async def get_weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
            city = ' '.join(context.args)
            if not city:
                await update.message.reply_text("Please provide a city name.")
                return
            
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}') as response:
                    if response.status == 200:
                        data = await response.json()
                        temp = data['current']['temp_c']
                        condition = data['current']['condition']['text']
                        await update.message.reply_text(f"Weather in {city}: {condition}, {temp}°C")
                    else:
                        await update.message.reply_text("Couldn't retrieve weather information.")
        ```
        
        ### Deploying Your Bot
        
        For production use, deploy your bot to a reliable server:
        
        1. Set up a virtual environment
        2. Use a process manager like Supervisor or PM2
        3. Consider using webhooks instead of polling for better performance
        
        ### Conclusion
        
        Telegram bots offer a versatile platform for creating interactive services. With Python's elegant syntax and 
        powerful libraries, you can build sophisticated bots that deliver real value to users.
        
        In future posts, I'll explore advanced topics like natural language processing integration and scaling bots 
        for large user bases.
        """
    },
    {
        "title": "Optimizing Python Performance for Data Processing",
        "date": "2023-07-05",
        "category": "Python",
        "tags": ["Python", "Performance", "Optimization"],
        "content": """
        ## Optimizing Python Performance for Data Processing
        
        Python is known for its simplicity and readability, but these qualities sometimes come at the cost of performance. 
        In this article, I'll share strategies for optimizing Python code, especially for data processing tasks.
        
        ### Understanding Performance Bottlenecks
        
        Before optimizing, it's essential to identify where your code is spending the most time. Python provides several profiling tools:
        
        ```python
        import cProfile
        
        def my_function():
            # Your code here
            pass
        
        cProfile.run('my_function()')
        ```
        
        For more detailed information, you can use line profilers or memory profilers to pinpoint specific bottlenecks.
        
        ### Vectorization with NumPy
        
        One of the most effective ways to speed up numerical computations is to use NumPy's vectorized operations:
        
        ```python
        # Slow, iterative approach
        result = []
        for i in range(len(data)):
            result.append(data[i] * 2 + 5)
            
        # Fast, vectorized approach
        import numpy as np
        result = data * 2 + 5
        ```
        
        Vectorized operations execute in compiled C code, making them much faster than Python loops.
        
        ### Pandas Optimization Techniques
        
        For data processing with Pandas, several practices can significantly improve performance:
        
        #### Use Efficient Data Types
        
        ```python
        # Check memory usage
        df.info(memory_usage='deep')
        
        # Convert to appropriate dtypes
        df['category_column'] = df['category_column'].astype('category')
        df['integer_column'] = df['integer_column'].astype('int32')
        ```
        
        #### Vectorized String Operations
        
        ```python
        # Slow approach
        def clean_text(text):
            # Text processing
            return processed_text
            
        df['clean_text'] = df['text'].apply(clean_text)
        
        # Faster approach
        df['clean_text'] = df['text'].str.lower().str.replace('[^a-z0-9]', ' ')
        ```
        
        #### Use Query and Eval for Filtering
        
        ```python
        # Less efficient
        filtered_df = df[(df['column_a'] > 5) & (df['column_b'] == 'value')]
        
        # More efficient
        filtered_df = df.query('column_a > 5 and column_b == "value"')
        ```
        
        ### Parallel Processing with Multiprocessing
        
        For CPU-bound tasks, leveraging multiple cores can provide significant speedups:
        
        ```python
        from multiprocessing import Pool
        
        def process_chunk(chunk):
            # Process data chunk
            return result
            
        # Split data into chunks
        chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
        
        # Process in parallel
        with Pool(processes=4) as pool:
            results = pool.map(process_chunk, chunks)
            
        # Combine results
        final_result = combine_results(results)
        ```
        
        ### Just-In-Time Compilation with Numba
        
        For numerical algorithms, Numba can compile Python code to machine code:
        
        ```python
        from numba import jit
        
        @jit(nopython=True)
        def compute_intensive_function(x, y, z):
            # Numerical computation
            result = 0
            for i in range(len(x)):
                # Complex calculations
                result += x[i] * y[i] + z[i]
            return result
        ```
        
        This can yield 10-100x speedups for suitable functions.
        
        ### Cython for Critical Sections
        
        For the most performance-critical parts of your code, consider using Cython:
        
        ```python
        # cython_module.pyx
        import numpy as np
        cimport numpy as np
        
        def fast_function(np.ndarray[double, ndim=1] x, np.ndarray[double, ndim=1] y):
            cdef int i
            cdef int n = len(x)
            cdef double result = 0.0
            
            for i in range(n):
                result += x[i] * y[i]
                
            return result
        ```
        
        ### Real-world Example: Log Processing
        
        Let's combine several techniques to process a large log file:
        
        ```python
        import pandas as pd
        import numpy as np
        from multiprocessing import Pool
        
        def process_log_chunk(chunk_file):
            # Read chunk
            df = pd.read_csv(chunk_file, parse_dates=['timestamp'])
            
            # Optimize memory usage
            df['status_code'] = df['status_code'].astype('int16')
            df['user_id'] = df['user_id'].astype('category')
            
            # Process data (vectorized operations)
            df['response_time_ms'] = df['response_time_s'] * 1000
            df['log_response_time'] = np.log1p(df['response_time_ms'])
            
            # Filter and aggregate
            result = (df.query('status_code >= 400')
                      .groupby(['user_id', pd.Grouper(key='timestamp', freq='1h')])
                      .agg({'status_code': 'count', 'response_time_ms': 'mean'})
                      .reset_index())
                      
            return result
            
        # Split large log file into chunks
        # ... code to split file ...
        
        # Process in parallel
        with Pool(processes=8) as pool:
            results = pool.map(process_log_chunk, chunk_files)
            
        # Combine results
        final_result = pd.concat(results)
        ```
        
        ### Conclusion
        
        Python doesn't have to be slow. By understanding the nature of your performance bottlenecks and applying 
        the right optimization techniques, you can achieve excellent performance while maintaining the readability 
        and simplicity that make Python so popular.
        
        Remember to profile before optimizing, and focus your efforts on the critical parts of your code that will 
        yield the most significant improvements.
        """
    }
]

# Convert to DataFrame
df_blog = pd.DataFrame(blog_posts)
df_blog['date'] = pd.to_datetime(df_blog['date'])
df_blog = df_blog.sort_values('date', ascending=False)

# Filter options
st.markdown("### Filter Blog Posts")
col1, col2 = st.columns(2)

with col1:
    categories = sorted(df_blog["category"].unique())
    selected_categories = st.multiselect("Categories", categories, default=categories)

with col2:
    all_tags = sorted(list(set([tag for post in blog_posts for tag in post["tags"]])))
    selected_tags = st.multiselect("Tags", all_tags)

# Filter posts
filtered_posts = df_blog.copy()
if selected_categories:
    filtered_posts = filtered_posts[filtered_posts["category"].isin(selected_categories)]
if selected_tags:
    filtered_posts = filtered_posts[filtered_posts["tags"].apply(lambda x: any(tag in x for tag in selected_tags))]

# Display posts
if not filtered_posts.empty:
    # Display posts
    for i, row in filtered_posts.iterrows():
        with st.expander(f"{row['title']} ({row['date'].strftime('%Y-%m-%d')})"):
            st.markdown(f"**Category:** {row['category']} | **Tags:** {', '.join(row['tags'])}")
            st.markdown(row['content'])
            st.markdown(f"*Published on {row['date'].strftime('%B %d, %Y')}*")
else:
    st.info("No blog posts match the selected filters. Please adjust your criteria.")

# Display visitor counter at the bottom
display_visitor_counter()
