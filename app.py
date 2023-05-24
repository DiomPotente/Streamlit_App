import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def correct_grammar(input_string):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Correct this to standard English: " + input_string + "\n",
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        temperature=0.0,
        stop="\n\n",
    )
    answer = response.choices[0].text.strip()
    return answer


def main():
    st.title("Grammar Correction App")
    input_text = st.text_area("Enter a sentence:")
    st.text("Diomedes L. Potente BSCS 3A")
    
    if st.button("Correct Grammar"):
        corrected_text = correct_grammar(input_text)
        st.success("Corrected Sentence:")
        st.write(corrected_text)


if __name__ == "__main__":
    main()
