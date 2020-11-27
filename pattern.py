import lcs_naive


class Pattern:

    def __init__(self, prefix_to_remove, prefix_to_add, suffix_to_remove, suffix_to_add,
                 keep_source=True):
        self.keep_source = keep_source
        self.prefix_to_remove = prefix_to_remove
        self.prefix_to_add = prefix_to_add
        self.suffix_to_remove = suffix_to_remove
        self.suffix_to_add = suffix_to_add
        if not self.keep_source:
            self.prefix_to_remove = "." * len(self.prefix_to_remove)
            self.suffix_to_remove = "." * len(self.suffix_to_remove)

    def apply(self, s):
        if s.startswith(self.prefix_to_remove) and s.endswith(self.suffix_to_remove) or not self.keep_source:
            if len(self.prefix_to_remove) + len(self.suffix_to_remove) <= len(s):
                stem = s[len(self.prefix_to_remove):(len(s)-len(self.suffix_to_remove))]
                return self.prefix_to_add + stem + self.suffix_to_add
        return None

    def __str__(self):
        return "__".join([self.prefix_to_remove, self.prefix_to_add, self.suffix_to_remove, self.suffix_to_add])

    def __hash__(self):
         return hash(str(self))

    def __lt__(self, other):
        return hash(self) < hash(other)

    def __eq__(self, other):
        return hash(self) == hash(other)


def extract_pattern(first, second, method="naive_substring", keep_source=True):
    if method == "naive_substring":
        func = lcs_naive.longest_common_substring
    else:
        raise NotImplementedError()
    match = func(first, second)
    if "substring" in method:
        answer = Pattern(first[:match["first_start"]], second[:match["second_start"]],
                         first[match["first_end"]:], second[match["second_end"]:],
                         keep_source=keep_source)
    else:
        raise NotImplementedError()
    return answer