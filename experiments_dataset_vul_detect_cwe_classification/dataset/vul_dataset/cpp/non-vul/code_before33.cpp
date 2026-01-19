// Source: Row 145 in ./dataset/CVEfixes/Analysis/results/C++/df_cpp_all.xlsx

static void setAppend(SetType& set, const VariantType& v) {
auto value_type = type(v);
if (value_type != HPHP::serialize::Type::INT64 &&
    value_type != HPHP::serialize::Type::STRING) {
    throw HPHP::serialize::UnserializeError(
        "Unsupported keyset element of type " +
        folly::to<std::string>(value_type));
}
set.append(v);
}