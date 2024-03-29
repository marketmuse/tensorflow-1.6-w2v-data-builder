// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: tensorflow/core/protobuf/rewriter_config.proto

#ifndef PROTOBUF_tensorflow_2fcore_2fprotobuf_2frewriter_5fconfig_2eproto_INCLUDED
#define PROTOBUF_tensorflow_2fcore_2fprotobuf_2frewriter_5fconfig_2eproto_INCLUDED

#include <string>

#include <google/protobuf/stubs/common.h>

#if GOOGLE_PROTOBUF_VERSION < 3005000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please update
#error your headers.
#endif
#if 3005000 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_table_driven.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/metadata.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/generated_enum_reflection.h>
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)

namespace protobuf_tensorflow_2fcore_2fprotobuf_2frewriter_5fconfig_2eproto {
// Internal implementation detail -- do not use these members.
struct TableStruct {
  static const ::google::protobuf::internal::ParseTableField entries[];
  static const ::google::protobuf::internal::AuxillaryParseTableField aux[];
  static const ::google::protobuf::internal::ParseTable schema[2];
  static const ::google::protobuf::internal::FieldMetadata field_metadata[];
  static const ::google::protobuf::internal::SerializationTable serialization_table[];
  static const ::google::protobuf::uint32 offsets[];
};
void AddDescriptors();
void InitDefaultsAutoParallelOptionsImpl();
void InitDefaultsAutoParallelOptions();
void InitDefaultsRewriterConfigImpl();
void InitDefaultsRewriterConfig();
inline void InitDefaults() {
  InitDefaultsAutoParallelOptions();
  InitDefaultsRewriterConfig();
}
}  // namespace protobuf_tensorflow_2fcore_2fprotobuf_2frewriter_5fconfig_2eproto
namespace tensorflow {
class AutoParallelOptions;
class AutoParallelOptionsDefaultTypeInternal;
extern AutoParallelOptionsDefaultTypeInternal _AutoParallelOptions_default_instance_;
class RewriterConfig;
class RewriterConfigDefaultTypeInternal;
extern RewriterConfigDefaultTypeInternal _RewriterConfig_default_instance_;
}  // namespace tensorflow
namespace google {
namespace protobuf {
template<> ::tensorflow::AutoParallelOptions* Arena::CreateMessage< ::tensorflow::AutoParallelOptions>(Arena*);
template<> ::tensorflow::RewriterConfig* Arena::CreateMessage< ::tensorflow::RewriterConfig>(Arena*);
}  // namespace protobuf
}  // namespace google
namespace tensorflow {

enum RewriterConfig_Toggle {
  RewriterConfig_Toggle_DEFAULT = 0,
  RewriterConfig_Toggle_ON = 1,
  RewriterConfig_Toggle_OFF = 2,
  RewriterConfig_Toggle_AGGRESSIVE = 3,
  RewriterConfig_Toggle_RewriterConfig_Toggle_INT_MIN_SENTINEL_DO_NOT_USE_ = ::google::protobuf::kint32min,
  RewriterConfig_Toggle_RewriterConfig_Toggle_INT_MAX_SENTINEL_DO_NOT_USE_ = ::google::protobuf::kint32max
};
bool RewriterConfig_Toggle_IsValid(int value);
const RewriterConfig_Toggle RewriterConfig_Toggle_Toggle_MIN = RewriterConfig_Toggle_DEFAULT;
const RewriterConfig_Toggle RewriterConfig_Toggle_Toggle_MAX = RewriterConfig_Toggle_AGGRESSIVE;
const int RewriterConfig_Toggle_Toggle_ARRAYSIZE = RewriterConfig_Toggle_Toggle_MAX + 1;

const ::google::protobuf::EnumDescriptor* RewriterConfig_Toggle_descriptor();
inline const ::std::string& RewriterConfig_Toggle_Name(RewriterConfig_Toggle value) {
  return ::google::protobuf::internal::NameOfEnum(
    RewriterConfig_Toggle_descriptor(), value);
}
inline bool RewriterConfig_Toggle_Parse(
    const ::std::string& name, RewriterConfig_Toggle* value) {
  return ::google::protobuf::internal::ParseNamedEnum<RewriterConfig_Toggle>(
    RewriterConfig_Toggle_descriptor(), name, value);
}
enum RewriterConfig_MemOptType {
  RewriterConfig_MemOptType_DEFAULT_MEM_OPT = 0,
  RewriterConfig_MemOptType_NO_MEM_OPT = 1,
  RewriterConfig_MemOptType_MANUAL = 2,
  RewriterConfig_MemOptType_SWAPPING_HEURISTICS = 4,
  RewriterConfig_MemOptType_RECOMPUTATION_HEURISTICS = 5,
  RewriterConfig_MemOptType_SCHEDULING_HEURISTICS = 6,
  RewriterConfig_MemOptType_HEURISTICS = 3,
  RewriterConfig_MemOptType_RewriterConfig_MemOptType_INT_MIN_SENTINEL_DO_NOT_USE_ = ::google::protobuf::kint32min,
  RewriterConfig_MemOptType_RewriterConfig_MemOptType_INT_MAX_SENTINEL_DO_NOT_USE_ = ::google::protobuf::kint32max
};
bool RewriterConfig_MemOptType_IsValid(int value);
const RewriterConfig_MemOptType RewriterConfig_MemOptType_MemOptType_MIN = RewriterConfig_MemOptType_DEFAULT_MEM_OPT;
const RewriterConfig_MemOptType RewriterConfig_MemOptType_MemOptType_MAX = RewriterConfig_MemOptType_SCHEDULING_HEURISTICS;
const int RewriterConfig_MemOptType_MemOptType_ARRAYSIZE = RewriterConfig_MemOptType_MemOptType_MAX + 1;

const ::google::protobuf::EnumDescriptor* RewriterConfig_MemOptType_descriptor();
inline const ::std::string& RewriterConfig_MemOptType_Name(RewriterConfig_MemOptType value) {
  return ::google::protobuf::internal::NameOfEnum(
    RewriterConfig_MemOptType_descriptor(), value);
}
inline bool RewriterConfig_MemOptType_Parse(
    const ::std::string& name, RewriterConfig_MemOptType* value) {
  return ::google::protobuf::internal::ParseNamedEnum<RewriterConfig_MemOptType>(
    RewriterConfig_MemOptType_descriptor(), name, value);
}
// ===================================================================

class AutoParallelOptions : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:tensorflow.AutoParallelOptions) */ {
 public:
  AutoParallelOptions();
  virtual ~AutoParallelOptions();

  AutoParallelOptions(const AutoParallelOptions& from);

  inline AutoParallelOptions& operator=(const AutoParallelOptions& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  AutoParallelOptions(AutoParallelOptions&& from) noexcept
    : AutoParallelOptions() {
    *this = ::std::move(from);
  }

  inline AutoParallelOptions& operator=(AutoParallelOptions&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  inline ::google::protobuf::Arena* GetArena() const PROTOBUF_FINAL {
    return GetArenaNoVirtual();
  }
  inline void* GetMaybeArenaPointer() const PROTOBUF_FINAL {
    return MaybeArenaPtr();
  }
  static const ::google::protobuf::Descriptor* descriptor();
  static const AutoParallelOptions& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const AutoParallelOptions* internal_default_instance() {
    return reinterpret_cast<const AutoParallelOptions*>(
               &_AutoParallelOptions_default_instance_);
  }
  static PROTOBUF_CONSTEXPR int const kIndexInFileMessages =
    0;

  void UnsafeArenaSwap(AutoParallelOptions* other);
  void Swap(AutoParallelOptions* other);
  friend void swap(AutoParallelOptions& a, AutoParallelOptions& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline AutoParallelOptions* New() const PROTOBUF_FINAL {
    return ::google::protobuf::Arena::CreateMessage<AutoParallelOptions>(NULL);
  }

  AutoParallelOptions* New(::google::protobuf::Arena* arena) const PROTOBUF_FINAL {
    return ::google::protobuf::Arena::CreateMessage<AutoParallelOptions>(arena);
  }
  void CopyFrom(const ::google::protobuf::Message& from) PROTOBUF_FINAL;
  void MergeFrom(const ::google::protobuf::Message& from) PROTOBUF_FINAL;
  void CopyFrom(const AutoParallelOptions& from);
  void MergeFrom(const AutoParallelOptions& from);
  void Clear() PROTOBUF_FINAL;
  bool IsInitialized() const PROTOBUF_FINAL;

  size_t ByteSizeLong() const PROTOBUF_FINAL;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) PROTOBUF_FINAL;
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const PROTOBUF_FINAL;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* target) const PROTOBUF_FINAL;
  int GetCachedSize() const PROTOBUF_FINAL { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const PROTOBUF_FINAL;
  void InternalSwap(AutoParallelOptions* other);
  protected:
  explicit AutoParallelOptions(::google::protobuf::Arena* arena);
  private:
  static void ArenaDtor(void* object);
  inline void RegisterArenaDtor(::google::protobuf::Arena* arena);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return _internal_metadata_.arena();
  }
  inline void* MaybeArenaPtr() const {
    return _internal_metadata_.raw_arena_ptr();
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const PROTOBUF_FINAL;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // bool enable = 1;
  void clear_enable();
  static const int kEnableFieldNumber = 1;
  bool enable() const;
  void set_enable(bool value);

  // int32 num_replicas = 2;
  void clear_num_replicas();
  static const int kNumReplicasFieldNumber = 2;
  ::google::protobuf::int32 num_replicas() const;
  void set_num_replicas(::google::protobuf::int32 value);

  // @@protoc_insertion_point(class_scope:tensorflow.AutoParallelOptions)
 private:

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  template <typename T> friend class ::google::protobuf::Arena::InternalHelper;
  typedef void InternalArenaConstructable_;
  typedef void DestructorSkippable_;
  bool enable_;
  ::google::protobuf::int32 num_replicas_;
  mutable int _cached_size_;
  friend struct ::protobuf_tensorflow_2fcore_2fprotobuf_2frewriter_5fconfig_2eproto::TableStruct;
  friend void ::protobuf_tensorflow_2fcore_2fprotobuf_2frewriter_5fconfig_2eproto::InitDefaultsAutoParallelOptionsImpl();
};
// -------------------------------------------------------------------

class RewriterConfig : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:tensorflow.RewriterConfig) */ {
 public:
  RewriterConfig();
  virtual ~RewriterConfig();

  RewriterConfig(const RewriterConfig& from);

  inline RewriterConfig& operator=(const RewriterConfig& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  RewriterConfig(RewriterConfig&& from) noexcept
    : RewriterConfig() {
    *this = ::std::move(from);
  }

  inline RewriterConfig& operator=(RewriterConfig&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  inline ::google::protobuf::Arena* GetArena() const PROTOBUF_FINAL {
    return GetArenaNoVirtual();
  }
  inline void* GetMaybeArenaPointer() const PROTOBUF_FINAL {
    return MaybeArenaPtr();
  }
  static const ::google::protobuf::Descriptor* descriptor();
  static const RewriterConfig& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const RewriterConfig* internal_default_instance() {
    return reinterpret_cast<const RewriterConfig*>(
               &_RewriterConfig_default_instance_);
  }
  static PROTOBUF_CONSTEXPR int const kIndexInFileMessages =
    1;

  void UnsafeArenaSwap(RewriterConfig* other);
  void Swap(RewriterConfig* other);
  friend void swap(RewriterConfig& a, RewriterConfig& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline RewriterConfig* New() const PROTOBUF_FINAL {
    return ::google::protobuf::Arena::CreateMessage<RewriterConfig>(NULL);
  }

  RewriterConfig* New(::google::protobuf::Arena* arena) const PROTOBUF_FINAL {
    return ::google::protobuf::Arena::CreateMessage<RewriterConfig>(arena);
  }
  void CopyFrom(const ::google::protobuf::Message& from) PROTOBUF_FINAL;
  void MergeFrom(const ::google::protobuf::Message& from) PROTOBUF_FINAL;
  void CopyFrom(const RewriterConfig& from);
  void MergeFrom(const RewriterConfig& from);
  void Clear() PROTOBUF_FINAL;
  bool IsInitialized() const PROTOBUF_FINAL;

  size_t ByteSizeLong() const PROTOBUF_FINAL;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) PROTOBUF_FINAL;
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const PROTOBUF_FINAL;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* target) const PROTOBUF_FINAL;
  int GetCachedSize() const PROTOBUF_FINAL { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const PROTOBUF_FINAL;
  void InternalSwap(RewriterConfig* other);
  protected:
  explicit RewriterConfig(::google::protobuf::Arena* arena);
  private:
  static void ArenaDtor(void* object);
  inline void RegisterArenaDtor(::google::protobuf::Arena* arena);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return _internal_metadata_.arena();
  }
  inline void* MaybeArenaPtr() const {
    return _internal_metadata_.raw_arena_ptr();
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const PROTOBUF_FINAL;

  // nested types ----------------------------------------------------

  typedef RewriterConfig_Toggle Toggle;
  static const Toggle DEFAULT =
    RewriterConfig_Toggle_DEFAULT;
  static const Toggle ON =
    RewriterConfig_Toggle_ON;
  static const Toggle OFF =
    RewriterConfig_Toggle_OFF;
  static const Toggle AGGRESSIVE =
    RewriterConfig_Toggle_AGGRESSIVE;
  static inline bool Toggle_IsValid(int value) {
    return RewriterConfig_Toggle_IsValid(value);
  }
  static const Toggle Toggle_MIN =
    RewriterConfig_Toggle_Toggle_MIN;
  static const Toggle Toggle_MAX =
    RewriterConfig_Toggle_Toggle_MAX;
  static const int Toggle_ARRAYSIZE =
    RewriterConfig_Toggle_Toggle_ARRAYSIZE;
  static inline const ::google::protobuf::EnumDescriptor*
  Toggle_descriptor() {
    return RewriterConfig_Toggle_descriptor();
  }
  static inline const ::std::string& Toggle_Name(Toggle value) {
    return RewriterConfig_Toggle_Name(value);
  }
  static inline bool Toggle_Parse(const ::std::string& name,
      Toggle* value) {
    return RewriterConfig_Toggle_Parse(name, value);
  }

  typedef RewriterConfig_MemOptType MemOptType;
  static const MemOptType DEFAULT_MEM_OPT =
    RewriterConfig_MemOptType_DEFAULT_MEM_OPT;
  static const MemOptType NO_MEM_OPT =
    RewriterConfig_MemOptType_NO_MEM_OPT;
  static const MemOptType MANUAL =
    RewriterConfig_MemOptType_MANUAL;
  static const MemOptType SWAPPING_HEURISTICS =
    RewriterConfig_MemOptType_SWAPPING_HEURISTICS;
  static const MemOptType RECOMPUTATION_HEURISTICS =
    RewriterConfig_MemOptType_RECOMPUTATION_HEURISTICS;
  static const MemOptType SCHEDULING_HEURISTICS =
    RewriterConfig_MemOptType_SCHEDULING_HEURISTICS;
  static const MemOptType HEURISTICS =
    RewriterConfig_MemOptType_HEURISTICS;
  static inline bool MemOptType_IsValid(int value) {
    return RewriterConfig_MemOptType_IsValid(value);
  }
  static const MemOptType MemOptType_MIN =
    RewriterConfig_MemOptType_MemOptType_MIN;
  static const MemOptType MemOptType_MAX =
    RewriterConfig_MemOptType_MemOptType_MAX;
  static const int MemOptType_ARRAYSIZE =
    RewriterConfig_MemOptType_MemOptType_ARRAYSIZE;
  static inline const ::google::protobuf::EnumDescriptor*
  MemOptType_descriptor() {
    return RewriterConfig_MemOptType_descriptor();
  }
  static inline const ::std::string& MemOptType_Name(MemOptType value) {
    return RewriterConfig_MemOptType_Name(value);
  }
  static inline bool MemOptType_Parse(const ::std::string& name,
      MemOptType* value) {
    return RewriterConfig_MemOptType_Parse(name, value);
  }

  // accessors -------------------------------------------------------

  // repeated string optimizers = 100;
  int optimizers_size() const;
  void clear_optimizers();
  static const int kOptimizersFieldNumber = 100;
  const ::std::string& optimizers(int index) const;
  ::std::string* mutable_optimizers(int index);
  void set_optimizers(int index, const ::std::string& value);
  #if LANG_CXX11
  void set_optimizers(int index, ::std::string&& value);
  #endif
  void set_optimizers(int index, const char* value);
  void set_optimizers(int index, const char* value, size_t size);
  ::std::string* add_optimizers();
  void add_optimizers(const ::std::string& value);
  #if LANG_CXX11
  void add_optimizers(::std::string&& value);
  #endif
  void add_optimizers(const char* value);
  void add_optimizers(const char* value, size_t size);
  const ::google::protobuf::RepeatedPtrField< ::std::string>& optimizers() const;
  ::google::protobuf::RepeatedPtrField< ::std::string>* mutable_optimizers();

  // string memory_optimizer_target_node_name_prefix = 6;
  void clear_memory_optimizer_target_node_name_prefix();
  static const int kMemoryOptimizerTargetNodeNamePrefixFieldNumber = 6;
  const ::std::string& memory_optimizer_target_node_name_prefix() const;
  void set_memory_optimizer_target_node_name_prefix(const ::std::string& value);
  #if LANG_CXX11
  void set_memory_optimizer_target_node_name_prefix(::std::string&& value);
  #endif
  void set_memory_optimizer_target_node_name_prefix(const char* value);
  void set_memory_optimizer_target_node_name_prefix(const char* value, size_t size);
  ::std::string* mutable_memory_optimizer_target_node_name_prefix();
  ::std::string* release_memory_optimizer_target_node_name_prefix();
  void set_allocated_memory_optimizer_target_node_name_prefix(::std::string* memory_optimizer_target_node_name_prefix);
  PROTOBUF_RUNTIME_DEPRECATED("The unsafe_arena_ accessors for"
  "    string fields are deprecated and will be removed in a"
  "    future release.")
  ::std::string* unsafe_arena_release_memory_optimizer_target_node_name_prefix();
  PROTOBUF_RUNTIME_DEPRECATED("The unsafe_arena_ accessors for"
  "    string fields are deprecated and will be removed in a"
  "    future release.")
  void unsafe_arena_set_allocated_memory_optimizer_target_node_name_prefix(
      ::std::string* memory_optimizer_target_node_name_prefix);

  // .tensorflow.AutoParallelOptions auto_parallel = 5;
  bool has_auto_parallel() const;
  void clear_auto_parallel();
  static const int kAutoParallelFieldNumber = 5;
  const ::tensorflow::AutoParallelOptions& auto_parallel() const;
  ::tensorflow::AutoParallelOptions* release_auto_parallel();
  ::tensorflow::AutoParallelOptions* mutable_auto_parallel();
  void set_allocated_auto_parallel(::tensorflow::AutoParallelOptions* auto_parallel);
  void unsafe_arena_set_allocated_auto_parallel(
      ::tensorflow::AutoParallelOptions* auto_parallel);
  ::tensorflow::AutoParallelOptions* unsafe_arena_release_auto_parallel();

  // .tensorflow.RewriterConfig.Toggle layout_optimizer = 1;
  void clear_layout_optimizer();
  static const int kLayoutOptimizerFieldNumber = 1;
  ::tensorflow::RewriterConfig_Toggle layout_optimizer() const;
  void set_layout_optimizer(::tensorflow::RewriterConfig_Toggle value);

  // bool disable_model_pruning = 2;
  void clear_disable_model_pruning();
  static const int kDisableModelPruningFieldNumber = 2;
  bool disable_model_pruning() const;
  void set_disable_model_pruning(bool value);

  // .tensorflow.RewriterConfig.Toggle constant_folding = 3;
  void clear_constant_folding();
  static const int kConstantFoldingFieldNumber = 3;
  ::tensorflow::RewriterConfig_Toggle constant_folding() const;
  void set_constant_folding(::tensorflow::RewriterConfig_Toggle value);

  // .tensorflow.RewriterConfig.MemOptType memory_optimization = 4;
  void clear_memory_optimization();
  static const int kMemoryOptimizationFieldNumber = 4;
  ::tensorflow::RewriterConfig_MemOptType memory_optimization() const;
  void set_memory_optimization(::tensorflow::RewriterConfig_MemOptType value);

  // .tensorflow.RewriterConfig.Toggle arithmetic_optimization = 7;
  void clear_arithmetic_optimization();
  static const int kArithmeticOptimizationFieldNumber = 7;
  ::tensorflow::RewriterConfig_Toggle arithmetic_optimization() const;
  void set_arithmetic_optimization(::tensorflow::RewriterConfig_Toggle value);

  // .tensorflow.RewriterConfig.Toggle dependency_optimization = 8;
  void clear_dependency_optimization();
  static const int kDependencyOptimizationFieldNumber = 8;
  ::tensorflow::RewriterConfig_Toggle dependency_optimization() const;
  void set_dependency_optimization(::tensorflow::RewriterConfig_Toggle value);

  // @@protoc_insertion_point(class_scope:tensorflow.RewriterConfig)
 private:

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  template <typename T> friend class ::google::protobuf::Arena::InternalHelper;
  typedef void InternalArenaConstructable_;
  typedef void DestructorSkippable_;
  ::google::protobuf::RepeatedPtrField< ::std::string> optimizers_;
  ::google::protobuf::internal::ArenaStringPtr memory_optimizer_target_node_name_prefix_;
  ::tensorflow::AutoParallelOptions* auto_parallel_;
  int layout_optimizer_;
  bool disable_model_pruning_;
  int constant_folding_;
  int memory_optimization_;
  int arithmetic_optimization_;
  int dependency_optimization_;
  mutable int _cached_size_;
  friend struct ::protobuf_tensorflow_2fcore_2fprotobuf_2frewriter_5fconfig_2eproto::TableStruct;
  friend void ::protobuf_tensorflow_2fcore_2fprotobuf_2frewriter_5fconfig_2eproto::InitDefaultsRewriterConfigImpl();
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// AutoParallelOptions

// bool enable = 1;
inline void AutoParallelOptions::clear_enable() {
  enable_ = false;
}
inline bool AutoParallelOptions::enable() const {
  // @@protoc_insertion_point(field_get:tensorflow.AutoParallelOptions.enable)
  return enable_;
}
inline void AutoParallelOptions::set_enable(bool value) {
  
  enable_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.AutoParallelOptions.enable)
}

// int32 num_replicas = 2;
inline void AutoParallelOptions::clear_num_replicas() {
  num_replicas_ = 0;
}
inline ::google::protobuf::int32 AutoParallelOptions::num_replicas() const {
  // @@protoc_insertion_point(field_get:tensorflow.AutoParallelOptions.num_replicas)
  return num_replicas_;
}
inline void AutoParallelOptions::set_num_replicas(::google::protobuf::int32 value) {
  
  num_replicas_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.AutoParallelOptions.num_replicas)
}

// -------------------------------------------------------------------

// RewriterConfig

// .tensorflow.RewriterConfig.Toggle layout_optimizer = 1;
inline void RewriterConfig::clear_layout_optimizer() {
  layout_optimizer_ = 0;
}
inline ::tensorflow::RewriterConfig_Toggle RewriterConfig::layout_optimizer() const {
  // @@protoc_insertion_point(field_get:tensorflow.RewriterConfig.layout_optimizer)
  return static_cast< ::tensorflow::RewriterConfig_Toggle >(layout_optimizer_);
}
inline void RewriterConfig::set_layout_optimizer(::tensorflow::RewriterConfig_Toggle value) {
  
  layout_optimizer_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.RewriterConfig.layout_optimizer)
}

// .tensorflow.RewriterConfig.Toggle constant_folding = 3;
inline void RewriterConfig::clear_constant_folding() {
  constant_folding_ = 0;
}
inline ::tensorflow::RewriterConfig_Toggle RewriterConfig::constant_folding() const {
  // @@protoc_insertion_point(field_get:tensorflow.RewriterConfig.constant_folding)
  return static_cast< ::tensorflow::RewriterConfig_Toggle >(constant_folding_);
}
inline void RewriterConfig::set_constant_folding(::tensorflow::RewriterConfig_Toggle value) {
  
  constant_folding_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.RewriterConfig.constant_folding)
}

// .tensorflow.RewriterConfig.Toggle arithmetic_optimization = 7;
inline void RewriterConfig::clear_arithmetic_optimization() {
  arithmetic_optimization_ = 0;
}
inline ::tensorflow::RewriterConfig_Toggle RewriterConfig::arithmetic_optimization() const {
  // @@protoc_insertion_point(field_get:tensorflow.RewriterConfig.arithmetic_optimization)
  return static_cast< ::tensorflow::RewriterConfig_Toggle >(arithmetic_optimization_);
}
inline void RewriterConfig::set_arithmetic_optimization(::tensorflow::RewriterConfig_Toggle value) {
  
  arithmetic_optimization_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.RewriterConfig.arithmetic_optimization)
}

// .tensorflow.RewriterConfig.Toggle dependency_optimization = 8;
inline void RewriterConfig::clear_dependency_optimization() {
  dependency_optimization_ = 0;
}
inline ::tensorflow::RewriterConfig_Toggle RewriterConfig::dependency_optimization() const {
  // @@protoc_insertion_point(field_get:tensorflow.RewriterConfig.dependency_optimization)
  return static_cast< ::tensorflow::RewriterConfig_Toggle >(dependency_optimization_);
}
inline void RewriterConfig::set_dependency_optimization(::tensorflow::RewriterConfig_Toggle value) {
  
  dependency_optimization_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.RewriterConfig.dependency_optimization)
}

// bool disable_model_pruning = 2;
inline void RewriterConfig::clear_disable_model_pruning() {
  disable_model_pruning_ = false;
}
inline bool RewriterConfig::disable_model_pruning() const {
  // @@protoc_insertion_point(field_get:tensorflow.RewriterConfig.disable_model_pruning)
  return disable_model_pruning_;
}
inline void RewriterConfig::set_disable_model_pruning(bool value) {
  
  disable_model_pruning_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.RewriterConfig.disable_model_pruning)
}

// .tensorflow.RewriterConfig.MemOptType memory_optimization = 4;
inline void RewriterConfig::clear_memory_optimization() {
  memory_optimization_ = 0;
}
inline ::tensorflow::RewriterConfig_MemOptType RewriterConfig::memory_optimization() const {
  // @@protoc_insertion_point(field_get:tensorflow.RewriterConfig.memory_optimization)
  return static_cast< ::tensorflow::RewriterConfig_MemOptType >(memory_optimization_);
}
inline void RewriterConfig::set_memory_optimization(::tensorflow::RewriterConfig_MemOptType value) {
  
  memory_optimization_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.RewriterConfig.memory_optimization)
}

// string memory_optimizer_target_node_name_prefix = 6;
inline void RewriterConfig::clear_memory_optimizer_target_node_name_prefix() {
  memory_optimizer_target_node_name_prefix_.ClearToEmpty(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), GetArenaNoVirtual());
}
inline const ::std::string& RewriterConfig::memory_optimizer_target_node_name_prefix() const {
  // @@protoc_insertion_point(field_get:tensorflow.RewriterConfig.memory_optimizer_target_node_name_prefix)
  return memory_optimizer_target_node_name_prefix_.Get();
}
inline void RewriterConfig::set_memory_optimizer_target_node_name_prefix(const ::std::string& value) {
  
  memory_optimizer_target_node_name_prefix_.Set(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), value, GetArenaNoVirtual());
  // @@protoc_insertion_point(field_set:tensorflow.RewriterConfig.memory_optimizer_target_node_name_prefix)
}
#if LANG_CXX11
inline void RewriterConfig::set_memory_optimizer_target_node_name_prefix(::std::string&& value) {
  
  memory_optimizer_target_node_name_prefix_.Set(
    &::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::move(value), GetArenaNoVirtual());
  // @@protoc_insertion_point(field_set_rvalue:tensorflow.RewriterConfig.memory_optimizer_target_node_name_prefix)
}
#endif
inline void RewriterConfig::set_memory_optimizer_target_node_name_prefix(const char* value) {
  GOOGLE_DCHECK(value != NULL);
  
  memory_optimizer_target_node_name_prefix_.Set(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(value),
              GetArenaNoVirtual());
  // @@protoc_insertion_point(field_set_char:tensorflow.RewriterConfig.memory_optimizer_target_node_name_prefix)
}
inline void RewriterConfig::set_memory_optimizer_target_node_name_prefix(const char* value,
    size_t size) {
  
  memory_optimizer_target_node_name_prefix_.Set(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(
      reinterpret_cast<const char*>(value), size), GetArenaNoVirtual());
  // @@protoc_insertion_point(field_set_pointer:tensorflow.RewriterConfig.memory_optimizer_target_node_name_prefix)
}
inline ::std::string* RewriterConfig::mutable_memory_optimizer_target_node_name_prefix() {
  
  // @@protoc_insertion_point(field_mutable:tensorflow.RewriterConfig.memory_optimizer_target_node_name_prefix)
  return memory_optimizer_target_node_name_prefix_.Mutable(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), GetArenaNoVirtual());
}
inline ::std::string* RewriterConfig::release_memory_optimizer_target_node_name_prefix() {
  // @@protoc_insertion_point(field_release:tensorflow.RewriterConfig.memory_optimizer_target_node_name_prefix)
  
  return memory_optimizer_target_node_name_prefix_.Release(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), GetArenaNoVirtual());
}
inline void RewriterConfig::set_allocated_memory_optimizer_target_node_name_prefix(::std::string* memory_optimizer_target_node_name_prefix) {
  if (memory_optimizer_target_node_name_prefix != NULL) {
    
  } else {
    
  }
  memory_optimizer_target_node_name_prefix_.SetAllocated(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), memory_optimizer_target_node_name_prefix,
      GetArenaNoVirtual());
  // @@protoc_insertion_point(field_set_allocated:tensorflow.RewriterConfig.memory_optimizer_target_node_name_prefix)
}
inline ::std::string* RewriterConfig::unsafe_arena_release_memory_optimizer_target_node_name_prefix() {
  // @@protoc_insertion_point(field_unsafe_arena_release:tensorflow.RewriterConfig.memory_optimizer_target_node_name_prefix)
  GOOGLE_DCHECK(GetArenaNoVirtual() != NULL);
  
  return memory_optimizer_target_node_name_prefix_.UnsafeArenaRelease(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      GetArenaNoVirtual());
}
inline void RewriterConfig::unsafe_arena_set_allocated_memory_optimizer_target_node_name_prefix(
    ::std::string* memory_optimizer_target_node_name_prefix) {
  GOOGLE_DCHECK(GetArenaNoVirtual() != NULL);
  if (memory_optimizer_target_node_name_prefix != NULL) {
    
  } else {
    
  }
  memory_optimizer_target_node_name_prefix_.UnsafeArenaSetAllocated(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      memory_optimizer_target_node_name_prefix, GetArenaNoVirtual());
  // @@protoc_insertion_point(field_unsafe_arena_set_allocated:tensorflow.RewriterConfig.memory_optimizer_target_node_name_prefix)
}

// .tensorflow.AutoParallelOptions auto_parallel = 5;
inline bool RewriterConfig::has_auto_parallel() const {
  return this != internal_default_instance() && auto_parallel_ != NULL;
}
inline void RewriterConfig::clear_auto_parallel() {
  if (GetArenaNoVirtual() == NULL && auto_parallel_ != NULL) {
    delete auto_parallel_;
  }
  auto_parallel_ = NULL;
}
inline const ::tensorflow::AutoParallelOptions& RewriterConfig::auto_parallel() const {
  const ::tensorflow::AutoParallelOptions* p = auto_parallel_;
  // @@protoc_insertion_point(field_get:tensorflow.RewriterConfig.auto_parallel)
  return p != NULL ? *p : *reinterpret_cast<const ::tensorflow::AutoParallelOptions*>(
      &::tensorflow::_AutoParallelOptions_default_instance_);
}
inline ::tensorflow::AutoParallelOptions* RewriterConfig::release_auto_parallel() {
  // @@protoc_insertion_point(field_release:tensorflow.RewriterConfig.auto_parallel)
  
  ::tensorflow::AutoParallelOptions* temp = auto_parallel_;
  if (GetArenaNoVirtual() != NULL) {
    temp = ::google::protobuf::internal::DuplicateIfNonNull(temp, NULL);
  }
  auto_parallel_ = NULL;
  return temp;
}
inline ::tensorflow::AutoParallelOptions* RewriterConfig::unsafe_arena_release_auto_parallel() {
  // @@protoc_insertion_point(field_unsafe_arena_release:tensorflow.RewriterConfig.auto_parallel)
  
  ::tensorflow::AutoParallelOptions* temp = auto_parallel_;
  auto_parallel_ = NULL;
  return temp;
}
inline ::tensorflow::AutoParallelOptions* RewriterConfig::mutable_auto_parallel() {
  
  if (auto_parallel_ == NULL) {
    auto_parallel_ = ::google::protobuf::Arena::CreateMessage< ::tensorflow::AutoParallelOptions >(
        GetArenaNoVirtual());
  }
  // @@protoc_insertion_point(field_mutable:tensorflow.RewriterConfig.auto_parallel)
  return auto_parallel_;
}
inline void RewriterConfig::set_allocated_auto_parallel(::tensorflow::AutoParallelOptions* auto_parallel) {
  ::google::protobuf::Arena* message_arena = GetArenaNoVirtual();
  if (message_arena == NULL) {
    delete auto_parallel_;
  }
  if (auto_parallel) {
    ::google::protobuf::Arena* submessage_arena =
      ::google::protobuf::Arena::GetArena(auto_parallel);
    if (message_arena != submessage_arena) {
      auto_parallel = ::google::protobuf::internal::GetOwnedMessage(
          message_arena, auto_parallel, submessage_arena);
    }
    
  } else {
    
  }
  auto_parallel_ = auto_parallel;
  // @@protoc_insertion_point(field_set_allocated:tensorflow.RewriterConfig.auto_parallel)
}

// repeated string optimizers = 100;
inline int RewriterConfig::optimizers_size() const {
  return optimizers_.size();
}
inline void RewriterConfig::clear_optimizers() {
  optimizers_.Clear();
}
inline const ::std::string& RewriterConfig::optimizers(int index) const {
  // @@protoc_insertion_point(field_get:tensorflow.RewriterConfig.optimizers)
  return optimizers_.Get(index);
}
inline ::std::string* RewriterConfig::mutable_optimizers(int index) {
  // @@protoc_insertion_point(field_mutable:tensorflow.RewriterConfig.optimizers)
  return optimizers_.Mutable(index);
}
inline void RewriterConfig::set_optimizers(int index, const ::std::string& value) {
  // @@protoc_insertion_point(field_set:tensorflow.RewriterConfig.optimizers)
  optimizers_.Mutable(index)->assign(value);
}
#if LANG_CXX11
inline void RewriterConfig::set_optimizers(int index, ::std::string&& value) {
  // @@protoc_insertion_point(field_set:tensorflow.RewriterConfig.optimizers)
  optimizers_.Mutable(index)->assign(std::move(value));
}
#endif
inline void RewriterConfig::set_optimizers(int index, const char* value) {
  GOOGLE_DCHECK(value != NULL);
  optimizers_.Mutable(index)->assign(value);
  // @@protoc_insertion_point(field_set_char:tensorflow.RewriterConfig.optimizers)
}
inline void RewriterConfig::set_optimizers(int index, const char* value, size_t size) {
  optimizers_.Mutable(index)->assign(
    reinterpret_cast<const char*>(value), size);
  // @@protoc_insertion_point(field_set_pointer:tensorflow.RewriterConfig.optimizers)
}
inline ::std::string* RewriterConfig::add_optimizers() {
  // @@protoc_insertion_point(field_add_mutable:tensorflow.RewriterConfig.optimizers)
  return optimizers_.Add();
}
inline void RewriterConfig::add_optimizers(const ::std::string& value) {
  optimizers_.Add()->assign(value);
  // @@protoc_insertion_point(field_add:tensorflow.RewriterConfig.optimizers)
}
#if LANG_CXX11
inline void RewriterConfig::add_optimizers(::std::string&& value) {
  optimizers_.Add(std::move(value));
  // @@protoc_insertion_point(field_add:tensorflow.RewriterConfig.optimizers)
}
#endif
inline void RewriterConfig::add_optimizers(const char* value) {
  GOOGLE_DCHECK(value != NULL);
  optimizers_.Add()->assign(value);
  // @@protoc_insertion_point(field_add_char:tensorflow.RewriterConfig.optimizers)
}
inline void RewriterConfig::add_optimizers(const char* value, size_t size) {
  optimizers_.Add()->assign(reinterpret_cast<const char*>(value), size);
  // @@protoc_insertion_point(field_add_pointer:tensorflow.RewriterConfig.optimizers)
}
inline const ::google::protobuf::RepeatedPtrField< ::std::string>&
RewriterConfig::optimizers() const {
  // @@protoc_insertion_point(field_list:tensorflow.RewriterConfig.optimizers)
  return optimizers_;
}
inline ::google::protobuf::RepeatedPtrField< ::std::string>*
RewriterConfig::mutable_optimizers() {
  // @@protoc_insertion_point(field_mutable_list:tensorflow.RewriterConfig.optimizers)
  return &optimizers_;
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__
// -------------------------------------------------------------------


// @@protoc_insertion_point(namespace_scope)

}  // namespace tensorflow

namespace google {
namespace protobuf {

template <> struct is_proto_enum< ::tensorflow::RewriterConfig_Toggle> : ::google::protobuf::internal::true_type {};
template <>
inline const EnumDescriptor* GetEnumDescriptor< ::tensorflow::RewriterConfig_Toggle>() {
  return ::tensorflow::RewriterConfig_Toggle_descriptor();
}
template <> struct is_proto_enum< ::tensorflow::RewriterConfig_MemOptType> : ::google::protobuf::internal::true_type {};
template <>
inline const EnumDescriptor* GetEnumDescriptor< ::tensorflow::RewriterConfig_MemOptType>() {
  return ::tensorflow::RewriterConfig_MemOptType_descriptor();
}

}  // namespace protobuf
}  // namespace google

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_tensorflow_2fcore_2fprotobuf_2frewriter_5fconfig_2eproto_INCLUDED
