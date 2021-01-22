from DocumentSimilarity import DocumentSimilarity
import argparse


def execute_similarity_check(text_one, text_two):
    """ Function to call the similarity check method from DocumentSimilarity """
    doc_obj = DocumentSimilarity()
    similarity_score = doc_obj.similarity_score(text_one, text_two)
    print(
        "The similarity score between the provided text snippets is: {0} ".format(
            similarity_score
        )
    )


def arg_declarartion():
    """ Function to declare arguments to be taken """
    parser = argparse.ArgumentParser(
        description="""
    This script is going to create an employee profile. 
    """
    )
    parser.add_argument("text_one", help="First Text Snippet")
    parser.add_argument("text_two", help="Second Text Snippet")
    return parser


def argument_retrieval(args):
    """ Function to retrieve arguments from the parsed args """
    text_one = args.text_one
    text_two = args.text_two
    return text_one, text_two


def driver_function():
    """ Driver function to execute similarity check from
    command line """
    simObj = DocumentSimilarity()
    parser = arg_declarartion()
    args = parser.parse_args()
    text_one, text_two = argument_retrieval(args)
    execute_similarity_check(text_one, text_two)


if __name__ == "__main__":
    driver_function()
