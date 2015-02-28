# Given an array return all subsequences -> combinations

def subsequences(A, partial=None):
  result = []
  for i in range(len(A)):
    for j in range(len(result)):
      result.append([A[i]] + result[j])
    result.append([A[i]])
  return result

print subsequences([1, 2, 3])

# public ArrayList<String> getCombinations(String text) {
#     ArrayList<String> results = new ArrayList<String>();
#     for (int i = 0; i < text.length(); i++) {
#         // Record size as we will be adding to the list
#         int resultsLength = results.size();
#         for (int j = 0; j < resultsLength; j++) {
#             results.add(text.charAt(i) + results.get(j));
#         }
#         results.add(Character.toString(text.charAt(i)));
#     }
#     return results;
# }
